#Note: In MICA, a Lunar conjunction or a planetary conjunction occurs when the two celestial bodies have the same apparent geocentric right ascension.

from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

planet_list_top=[mercury, venus, mars, jupiter, saturn, uranus, neptune]

planet_name_list_eng=['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_name_list_chi=['水星', '金星', '火星', '木星', '土星', '天王星', '海王星']
list_planetary_appulse=[]
for i in range(len(planet_list_top)):
    for j in range(len(planet_list_top)):
        if i < j:
            def planetary_appulse_at(t):
                # e = earth.at(t) # Observe from geocentre
                e = (earth + HKO).at(t) # Observe from HKO
                s = e.observe(planet_list_top[i]).apparent()
                m = e.observe(planet_list_top[j]).apparent()
                return s.separation_from(m).degrees
            
            
            planetary_appulse_at.step_days = 5.0
            planetary_appulse_times, planetary_appulse = find_minima(t0, t1, planetary_appulse_at)

            for t, planetary_appulse_degrees in zip(planetary_appulse_times, planetary_appulse):
                sun_position=earth.at(t).observe(sun).apparent()
                if planetary_appulse_degrees <5: # only speration of less than this degrees will be found
                
                    temp_list_planetary_appulse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
                    temp_list_planetary_appulse[2]=t.astimezone(HKT).date()
                    temp_list_planetary_appulse[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
                    temp_list_planetary_appulse[4]='角距 Angular separation: ' + str("%0.2f" % planetary_appulse_degrees) +'°'
                    temp_list_planetary_appulse[1]=planet_name_list_eng[i] + '-'+ planet_name_list_eng[j]+ ' Appulse '
                    temp_list_planetary_appulse[0]=planet_name_list_chi[i] + '、'+ planet_name_list_chi[j]+ '最小角距'
                    temp_list_planetary_appulse[5]='?'
                    if int(earth.at(t).observe(planet_list_top[i]).separation_from(sun_position).degrees) < 30:
                        temp_list_planetary_appulse[5]=3
                    elif int(earth.at(t).observe(planet_list_top[i]).separation_from(sun_position).degrees) < 60:
                        if planetary_appulse_degrees < 1:
                            temp_list_planetary_appulse[5]=1
                        else:
                            temp_list_planetary_appulse[5]=2
                    else:
                        temp_list_planetary_appulse[5]=1
                    if j == 5 or j == 6:
                        temp_list_planetary_appulse[5]=3
                    print(temp_list_planetary_appulse)
                    list_planetary_appulse.append(temp_list_planetary_appulse)
