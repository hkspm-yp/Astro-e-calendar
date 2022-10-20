from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

planet_list=[mercury, venus, mars, jupiter, saturn, uranus, neptune]

planet_name_list_eng=['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
planet_name_list_chi=['水星', '金星', '火星', '木星', '土星', '天王星', '海王星']
list_planetary_conjunctions=[]
for i in range(len(planet_list)):
    for j in range(len(planet_list)):
        if i < j:
            def planetary_conjunctions_at(t):
                e = earth.at(t)
                s = e.observe(planet_list[i]).apparent()
                m = e.observe(planet_list[j]).apparent()
                sRa, _, _ = s.radec(epoch = 'date')
                mRa, _, _ = m.radec(epoch = 'date')
                return abs(sRa.hours - mRa.hours)
            planetary_conjunctions_at.step_days = 15.0
            planetary_conjunctions_times, planetary_conjunctions = find_minima(t0, t1, planetary_conjunctions_at)

            for t, planetary_conjunctions_degrees in zip(planetary_conjunctions_times, planetary_conjunctions):
                if planetary_conjunctions_degrees < 0.1:
                    # temp_list_planetary_conjunctions=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi', '8=level']
                    temp_list_planetary_conjunctions=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
                    temp_list_planetary_conjunctions[2]=t.astimezone(HKT).date()
                    temp_list_planetary_conjunctions[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
                    temp_list_planetary_conjunctions[4]=''
                    temp_list_planetary_conjunctions[1]=planet_name_list_eng[i] + ' '+ planet_name_list_eng[j]+ ' conjunction '+' (' + str( "%0.2f" % planetary_conjunctions_degrees) +'°)'
                    temp_list_planetary_conjunctions[0]=planet_name_list_chi[i] + '合'+ planet_name_list_chi[j]+  '(' + str( "%0.2f" % planetary_conjunctions_degrees) +'°)'
                    temp_list_planetary_conjunctions[5]='?'
                    if j == 5 or j == 6:
                        temp_list_planetary_conjunctions[5]=3
                    print(temp_list_planetary_conjunctions)
                    list_planetary_conjunctions.append(temp_list_planetary_conjunctions)