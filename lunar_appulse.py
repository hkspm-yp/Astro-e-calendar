 # This script considers special Planetary lunar appulse events which fulfill the following:
 # (1) the separation is less than 1 degree;
 # (2) the moon is above the horizon; 
 # (3) The Sun is 15 degrees below the horizon.


from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone
import numpy as np

planet_list=[mercury, venus, mars, jupiter, saturn, uranus, neptune]
name_list_chi=['水星、月球最小角距', '金星、月球最小角距', '火星、月球最小角距', '木星、月球最小角距', '土星、月球最小角距', '天王星、月球最小角距','海王星、月球最小角距']
name_list_eng=['Mercury-Moon Appulse',
               'Venus-Moon Appulse',
               'Mars-Moon Appulse',
               'Jupiter-Moon Appulse',
               'Saturn-Moon Appulse',
               'Uranus-Moon Appulse',
               'Neptune-Moon Appulse']
list_lunar_appulse=[]

def separation_at(t):
    # e = earth.at(t) # Observe from geocentre
    e = (earth + HKO).at(t) # Observe from HKO
    s = e.observe(moon).apparent()
    m = e.observe(planet_list[i]).apparent()
    return s.separation_from(m).degrees

separation_at.step_days = 15.0

for i in range(7):
    
    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        e = (earth + HKO).at(t)
        m = e.observe(moon).apparent().altaz()[0].degrees
        s = e.observe(sun).apparent().altaz()[0].degrees
        moon_distance=e.observe(moon).apparent().distance().km
        moon_angular_radius_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)
        if separation_degrees<1 and m >0 and s <-15: # change the conditions by the values here.
            temp_list_lunar_appulse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_lunar_appulse[2]=t.astimezone(HKT).date()
            temp_list_lunar_appulse[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
            temp_list_lunar_appulse[4]='角距 Angular separation: ' + str("%0.2f"% separation_degrees) +'°'
            temp_list_lunar_appulse[1]=name_list_eng[i]
            temp_list_lunar_appulse[0]=name_list_chi[i]
            if separation_degrees<moon_angular_radius_degrees:
                temp_list_lunar_appulse[0]=name_list_chi[i]+'(掩)'
                temp_list_lunar_appulse[1]=name_list_eng[i]+'(Occultation)'
            temp_list_lunar_appulse[5]='?'
            phase = almanac.moon_phase(eph, t)
            # if i ==0 or i == 5 or i == 6:
            #     temp_list_lunar_appulse[8]='3' 
            # if i == 2 or i ==3 or i ==4: # Mars, jupiter and saturn
            if phase.degrees > 330 or phase.degrees <30 or i==5 or i==6:
                temp_list_lunar_appulse[5]=3
            elif phase.degrees > 300 or phase.degrees <60:
                temp_list_lunar_appulse[5]=2
            else:
                temp_list_lunar_appulse[5]=1
            print(temp_list_lunar_appulse)
            phase = almanac.moon_phase(eph, t)
            list_lunar_appulse.append(temp_list_lunar_appulse)      
