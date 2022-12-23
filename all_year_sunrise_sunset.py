from datetime import datetime
from main import *
# Note: The earliest or lateset sunrise or sunset are not the same at different latitudes.
# t0 = ts.utc(2021, 1, 1)
# t1 = ts.utc(2021, 1, 22)
t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, HKO))

temp_list_sunset=['0','0','0','0','0','0']
temp_list_sunrise=['0','0','0','0','0','0']
list_sunrise=[]
list_sunset=[]

for yi, ti in zip(y, t):
    if yi==1:
        temp_list_sunrise=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_sunrise[0]='日出'
        temp_list_sunrise[1]='Sunrise'
        temp_list_sunrise[2]=ti.astimezone(HKT).date()
        temp_list_sunrise[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
        # temp_list_sunrise[3]=ti.astimezone(HKT).time().isoformat()
        temp_list_sunrise[4]=''
        temp_list_sunrise[5]=''
        
        print(temp_list_sunrise)
        list_sunrise.append(temp_list_sunrise)


    if yi==0:
        temp_list_sunset=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_sunset[0]='日落'
        temp_list_sunset[1]='Sunset'
        temp_list_sunset[2]=ti.astimezone(HKT).date()
        temp_list_sunset[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
        # temp_list_sunset[3]=ti.astimezone(HKT).time().isoformat()
        temp_list_sunset[4]=''
        temp_list_sunset[5]=''
        
        print(temp_list_sunset)
        list_sunset.append(temp_list_sunset)