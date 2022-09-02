from datetime import datetime
from pytz import timezone
from skyfield.api import load
from skyfield import almanac
from main import eph, t0, t1, HKT

t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))
list_SEASON_EVENTS=[]
for yi, ti in zip(y, t):
    
    temp_list_SEASON_EVENTS=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','','5=level']
    if yi==0:
        temp_list_SEASON_EVENTS[0]='春分'
    if yi==1:
        temp_list_SEASON_EVENTS[0]='夏至'
    if yi==2:
        temp_list_SEASON_EVENTS[0]='秋分'
    if yi==3:
        temp_list_SEASON_EVENTS[0]='冬至'    
        
    temp_list_SEASON_EVENTS[1]=almanac.SEASON_EVENTS[yi]
    
    temp_list_SEASON_EVENTS[2]=ti.astimezone(HKT).date()
    temp_list_SEASON_EVENTS[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
    temp_list_SEASON_EVENTS[5]=1

    list_SEASON_EVENTS.append(temp_list_SEASON_EVENTS)
    print(temp_list_SEASON_EVENTS)