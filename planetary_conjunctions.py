from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

planet_list_top=[mercury, venus, mars, jupiter, saturn, uranus, neptune]
#planet_list_button=[mercury, venus, mars, jupiter, saturn, uranus, neptune]

planet_name_list_eng=['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
planet_name_list_chi=['水星', '金星', '火星', '木星', '土星', '天王星', '海王星']
list_planetary_conjunctions=[]
for i in range(len(planet_list_top)):
    for j in range(len(planet_list_top)):
        if i < j:
            def planetary_conjunctions_at(t):
                e = earth.at(t)
                s = e.observe(planet_list_top[i]).apparent()
                m = e.observe(planet_list_top[j]).apparent()
                return s.separation_from(m).degrees
            planetary_conjunctions_at.step_days = 15.0
            planetary_conjunctions_times, planetary_conjunctions = find_minima(t0, t1, planetary_conjunctions_at)

            for t, planetary_conjunctions_degrees in zip(planetary_conjunctions_times, planetary_conjunctions):
                if planetary_conjunctions_degrees <5:
                    temp_list_planetary_conjunctions=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
                    temp_list_planetary_conjunctions[0]=t.astimezone(HKT).year
                    temp_list_planetary_conjunctions[1]=t.astimezone(HKT).month
                    temp_list_planetary_conjunctions[2]=t.astimezone(HKT).day
                    temp_list_planetary_conjunctions[3]=t.astimezone(HKT).hour
                    temp_list_planetary_conjunctions[4]=t.astimezone(HKT).minute
                    temp_list_planetary_conjunctions[5]=int(t.astimezone(HKT).second)
                    temp_list_planetary_conjunctions[6]=planet_name_list_eng[i] + ' '+ planet_name_list_eng[j]+ ' conjunction '+' (' + str( "%0.2f" % planetary_conjunctions_degrees) +'°)'
                    temp_list_planetary_conjunctions[7]=planet_name_list_chi[i] + '合'+ planet_name_list_chi[j]+  '(' + str( "%0.2f" % planetary_conjunctions_degrees) +'°)'
                    print(temp_list_planetary_conjunctions)
                    list_planetary_conjunctions.append(temp_list_planetary_conjunctions)