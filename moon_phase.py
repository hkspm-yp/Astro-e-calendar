from skyfield import almanac
from pytz import timezone
from main import eph, t0, t1, HKT

t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
list_moon_phases=[]
for yi, ti in zip(y, t):
    #print(yi, almanac.moon_phases[yi], ti.astimezone(HKT)_iso(' '))
    temp_list_moon_phases=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
    temp_list_moon_phases[0]=ti.astimezone(HKT).year
    temp_list_moon_phases[1]=ti.astimezone(HKT).month
    temp_list_moon_phases[2]=ti.astimezone(HKT).day
    temp_list_moon_phases[3]=ti.astimezone(HKT).hour
    temp_list_moon_phases[4]=ti.astimezone(HKT).minute
    temp_list_moon_phases[5]=int(ti.astimezone(HKT).second)
    temp_list_moon_phases[6]=almanac.MOON_PHASES[yi]
    if yi==0:
        temp_list_moon_phases[7]='新月'
    if yi==1:
        temp_list_moon_phases[7]='上弦'
    if yi==2:
        temp_list_moon_phases[7]='滿月'
    if yi==3:
        temp_list_moon_phases[7]='下弦'
    print(temp_list_moon_phases)
    list_moon_phases.append(temp_list_moon_phases)