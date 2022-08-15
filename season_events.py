from datetime import datetime
from pytz import timezone
from skyfield.api import load
from skyfield import almanac
from main import eph, t0, t1, HKT

t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))
list_SEASON_EVENTS=[]
for yi, ti in zip(y, t):
    temp_list_SEASON_EVENTS=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
    temp_list_SEASON_EVENTS[0]=ti.astimezone(HKT).year
    temp_list_SEASON_EVENTS[1]=ti.astimezone(HKT).month
    temp_list_SEASON_EVENTS[2]=ti.astimezone(HKT).day
    temp_list_SEASON_EVENTS[3]=ti.astimezone(HKT).hour
    temp_list_SEASON_EVENTS[4]=ti.astimezone(HKT).minute
    temp_list_SEASON_EVENTS[5]=int(ti.astimezone(HKT).second)
    temp_list_SEASON_EVENTS[6]=almanac.SEASON_EVENTS[yi]
    if yi==0:
        temp_list_SEASON_EVENTS[7]='春分'
    if yi==1:
        temp_list_SEASON_EVENTS[7]='夏至'
    if yi==2:
        temp_list_SEASON_EVENTS[7]='秋分'
    if yi==3:
        temp_list_SEASON_EVENTS[7]='冬至'
    list_SEASON_EVENTS.append(temp_list_SEASON_EVENTS)
    print(temp_list_SEASON_EVENTS)