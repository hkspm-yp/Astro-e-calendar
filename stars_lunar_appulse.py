 # This script considers speical stars lunar appulse events which fulfill the following:
 # (1) the separation is less that 1 degree;
 # (2) the moon is above the horizon; 
 # (3) the Sun is 15 degrees below the horizon.


from skyfield.api import Star, load
from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone
import numpy as np

Earth_radius=6378.1366
k_IAU=0.2725076
moon_radius_km=Earth_radius*k_IAU

name_list_chi=['角宿一、月球最小角距', '軒轅十四、月球最小角距', '心宿二、月球最小角距', '畢宿五、月球最小角距', '北河三、月球最小角距']
name_list_eng=['Spica-Moon Appulse',
               'Regulus-Moon Appulse',
               'Antares-Moon Appulse',
               'Aldebaran-Moon Appulse',
               'Pollux-Moon Appulse',]
list_stars_appulse=[]
# RA and DEC from J(now at 2022). Not J(2000). Atmospheric refraction is not considered.
Spica = Star(ra_hours=(13, 26, 21.67), dec_degrees=(-11, 16, 37.1))
Regulus  = Star(ra_hours=(10, 9, 33.70), dec_degrees=(11, 51, 29.6))
Antares  = Star(ra_hours=(16, 30, 46.33), dec_degrees=(-26, 28, 53.4))
Aldebaran  = Star(ra_hours=(4, 37, 14.11), dec_degrees=(16, 33, 19.8))
Pollux  = Star(ra_hours=(7, 46, 41.86), dec_degrees=(27, 58, 12.1))
planet_list=[Spica, Regulus, Antares, Aldebaran, Pollux]

for i in range(5):
    def separation_at(t):
        # e = earth.at(t) # Observe from geocentre
        e = (earth + HKO).at(t) # Observe from HKO
        m = e.observe(moon).apparent()
        s = e.observe(planet_list[i]).apparent()
        return s.separation_from(m).degrees

    separation_at.step_days = 15.0
    
    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        e = (earth + HKO).at(t)
        m = e.observe(moon).apparent().altaz()[0].degrees
        s = e.observe(sun).apparent().altaz()[0].degrees
        moon_distance=e.observe(moon).apparent().distance().km
        moon_angular_radius_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)
        if separation_degrees<1 and m >0 and s <-15: # change the conditions by the values here.
        
            temp_list_stars_appulse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_stars_appulse[2]=t.astimezone(HKT).date()
            temp_list_stars_appulse[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
            phase = almanac.moon_phase(eph, t)
            # temp_list_stars_appulse[4]='角距 Angular separation: ' + str("%0.2f" % separation_degrees) +'°; ' + 'Phase degrees of the Moon is ' + str(int(phase.degrees))+'°'
            temp_list_stars_appulse[4]='角距 Angular separation: ' + str("%0.2f" % separation_degrees) +'°'
            temp_list_stars_appulse[1]=name_list_eng[i]
            temp_list_stars_appulse[0]=name_list_chi[i]
            if separation_degrees < moon_angular_radius_degrees:
                temp_list_stars_appulse[0]=name_list_chi[i]+'(掩)'
                temp_list_stars_appulse[1]=name_list_eng[i]+'(Occultation)'
                                
            temp_list_stars_appulse[5]='?'
            # if i ==0 or i == 5 or i == 6:
            #     temp_list_stars_appulse[8]='3' 
            # if i == 2 or i ==3 or i ==4: # Mars, jupiter and saturn
            if phase.degrees > 330 or phase.degrees <30:
                temp_list_stars_appulse[5]=3
            elif phase.degrees > 300 or phase.degrees <60:
                if separation_degrees < 1:
                    temp_list_stars_appulse[5]=1
                else:
                    temp_list_stars_appulse[5]=2
                temp_list_stars_appulse[5]=2
            else:
                temp_list_stars_appulse[5]=1
            print(temp_list_stars_appulse)
            phase = almanac.moon_phase(eph, t)
            list_stars_appulse.append(temp_list_stars_appulse)      
