from skyfield.api import Star, load
# planets = load('de440.bsp')
# earth = planets['earth']
# ts = load.timescale()
# t = ts.now()
# astrometric = earth.at(t).observe(barnard)
# ra, dec, distance = astrometric.radec()
# print(ra)
# print(dec)

from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

name_list_chi=['角宿一、月球最小角距', '軒轅十四、月球最小角距', '心宿二、月球最小角距', '畢宿五、月球最小角距', '北河三、月球最小角距']
name_list_eng=['Spica-Moon Appulse',
               'Regulus-Moon Appulse',
               'Antares-Moon Appulse',
               'Aldebaran-Moon Appulse',
               'Pollux-Moon Appulse',]
list_stars_appulse=[]
Spica = Star(ra_hours=(13, 26, 17), dec_degrees=(-11, 9, 40.5))
Regulus  = Star(ra_hours=(10, 8, 22.46), dec_degrees=(11, 58, 1.9))
Antares  = Star(ra_hours=(16, 29, 24.47), dec_degrees=(-26, 25, 55))
Aldebaran  = Star(ra_hours=(4, 35, 55.20), dec_degrees=(16, 30, 35.1))
Pollux  = Star(ra_hours=(7, 45, 19.36), dec_degrees=(28, 1, 34.7))
planet_list=[Spica, Regulus, Antares, Aldebaran, Pollux]

for i in range(5):
    def separation_at(t):
        # e = earth.at(t) # Observe from geocentre
        e = (earth + wgs84.latlon(22.3193 * N, 114.1694 * E)).at(t) # Observe from Hong Kong
        m = e.observe(moon).apparent()
        s = e.observe(planet_list[i]).apparent()
        return s.separation_from(m).degrees

    separation_at.step_days = 15.0
    
    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        temp_list_stars_appulse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_stars_appulse[2]=t.astimezone(HKT).date()
        temp_list_stars_appulse[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
        phase = almanac.moon_phase(eph, t)
        temp_list_stars_appulse[4]='Angular separation is ' + str("%0.2f" % separation_degrees) +'°; ' + 'Phase degrees of the Moon is ' + str(int(phase.degrees))+'°'
        temp_list_stars_appulse[1]=name_list_eng[i]
        temp_list_stars_appulse[0]=name_list_chi[i]
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