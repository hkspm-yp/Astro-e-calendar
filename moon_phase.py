from skyfield import almanac
from pytz import timezone
from main import *

t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
list_moon_phases=[]

def fullmoon_distance(t):
    e = earth.at(t)
    md = e.observe(moon).apparent()
    return md.distance().km
list_smallest_fullmoon=['全年最小滿月', 'Smallest fullmoon of the year','2=date(dd/mm/yyyy)','3=time(hh/mm)','0', 1]
list_largest_fullmoon=['全年最大滿月', 'Largest fullmoon of the year','2=date(dd/mm/yyyy)','3=time(hh/mm)','365000', 1]

for yi, ti in zip(y, t):
    #print(yi, almanac.moon_phases[yi], ti.astimezone(HKT)_iso(' '))
    temp_list_moon_phases=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_moon_phases[2]=ti.astimezone(HKT).date()
    temp_list_moon_phases[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
    temp_list_moon_phases[4]=''
    temp_list_moon_phases[1]=almanac.MOON_PHASES[yi]
    temp_list_moon_phases[5]=1
    if yi==0:
        temp_list_moon_phases[0]='新月'
    if yi==1:
        temp_list_moon_phases[0]='上弦'
    if yi==2:
        temp_list_moon_phases[0]='滿月'
        if float(fullmoon_distance(ti)) > float(list_smallest_fullmoon[4]):
            list_smallest_fullmoon[2]=ti.astimezone(HKT).date()
            list_smallest_fullmoon[4]= fullmoon_distance(ti)
            list_smallest_fullmoon[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24

        if float(fullmoon_distance(ti)) < float(list_largest_fullmoon[4]):
            list_largest_fullmoon[2]=ti.astimezone(HKT).date()
            list_largest_fullmoon[4]= fullmoon_distance(ti)
            list_largest_fullmoon[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
    if yi==3:
        temp_list_moon_phases[0]='下弦'
    print(temp_list_moon_phases)
    list_moon_phases.append(temp_list_moon_phases)
list_smallest_fullmoon[4]= str(int(list_smallest_fullmoon[4])) + ' km'
list_largest_fullmoon[4]= str(int(list_largest_fullmoon[4])) + ' km'
print(list_smallest_fullmoon)
print(list_largest_fullmoon)
list_moon_phases.append(list_smallest_fullmoon)
list_moon_phases.append(list_largest_fullmoon)