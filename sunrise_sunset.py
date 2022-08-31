from datetime import datetime
from main import *
bluffton = api.wgs84.latlon(+22.12, +114.22)
# t0 = ts.utc(2021, 5, 12, 4)
# t1 = ts.utc(2021, 7, 23, 4)
t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))
temp_list_sunset=['0','0','0','0','0','0']
temp_list_sunrise=['0','0','0','0','0','0']
temp_list_earliest_sunrise=['60','60','60','60','60','60']
temp_list_earliest_sunset=['60','60','60','60','60','60']
sunrise_sun=[]

# 全年最遲日出
for yi, ti in zip(y, t):
    if yi==1:
        if  ti.astimezone(HKT).month==1:

            if int(ti.astimezone(HKT).minute)>= int(temp_list_sunrise[4]):            
                if int(ti.astimezone(HKT).minute) == int(temp_list_sunrise[4]) and float(ti.astimezone(HKT).second) < float(temp_list_sunrise[5]):
                    break
                else:
                    temp_list_sunrise[2]=ti.astimezone(HKT).date()
                    temp_list_sunrise[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
                    temp_list_sunrise[4]=ti.astimezone(HKT).minute
                    temp_list_sunrise[5]=ti.astimezone(HKT).second
                    # print(temp_list_sunrise)
temp_list_sunrise[1]='Latest sunrise of the year'
temp_list_sunrise[0]='全年最遲日出'
temp_list_sunrise[4]=''
temp_list_sunrise[5]=1
print(temp_list_sunrise)
sunrise_sun.append(temp_list_sunrise)

for yi, ti in zip(y, t):
    if yi==0:
        if  ti.astimezone(HKT).month==7:

            if int(ti.astimezone(HKT).minute)>= int(temp_list_sunset[4]):            
                if int(ti.astimezone(HKT).minute) == int(temp_list_sunset[4]) and float(ti.astimezone(HKT).second) < float(temp_list_sunset[5]):
                    break
                else:
                    temp_list_sunset[2]=ti.astimezone(HKT).date()
                    temp_list_sunset[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
                    temp_list_sunset[4]=ti.astimezone(HKT).minute
                    temp_list_sunset[5]=ti.astimezone(HKT).second  
temp_list_sunset[1]='Latest sunset of the year'
temp_list_sunset[0]='全年最遲日落'
temp_list_sunset[4]=''   
temp_list_sunset[5]=1
print(temp_list_sunset)
sunrise_sun.append(temp_list_sunset)

for yi, ti in zip(y, t):
    if yi==1:
        if  ti.astimezone(HKT).month==6:

            if int(ti.astimezone(HKT).minute)<= int(temp_list_earliest_sunrise[4]):            
                if int(ti.astimezone(HKT).minute) == int(temp_list_earliest_sunrise[4]) and float(ti.astimezone(HKT).second) > float(temp_list_earliest_sunrise[5]):
                    break
                else:
                    temp_list_earliest_sunrise[2]=ti.astimezone(HKT).date()
                    temp_list_earliest_sunrise[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
                    temp_list_earliest_sunrise[4]=ti.astimezone(HKT).minute
                    temp_list_earliest_sunrise[5]=ti.astimezone(HKT).second
temp_list_earliest_sunrise[1]='Earliest sunrise of the year'
temp_list_earliest_sunrise[0]='全年最早日出'
temp_list_earliest_sunrise[4]=''
temp_list_earliest_sunrise[5]=1            
print(temp_list_earliest_sunrise)
sunrise_sun.append(temp_list_earliest_sunrise)

for yi, ti in zip(y, t):
    if yi==0:
        if  ti.astimezone(HKT).month == 12:
            temp_list_earliest_sunset[4]=ti.astimezone(HKT).minute
            temp_list_earliest_sunset[5]=ti.astimezone(HKT).second
            
            if int(ti.astimezone(HKT).minute)<= int(temp_list_earliest_sunset[4]):            
                if int(ti.astimezone(HKT).minute) == int(temp_list_earliest_sunset[4]) and float(ti.astimezone(HKT).second) > float(temp_list_earliest_sunset[5]):
                    break
                else:
                    temp_list_earliest_sunset[2]=ti.astimezone(HKT).date()
                    temp_list_earliest_sunset[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
                    temp_list_earliest_sunset[4]=ti.astimezone(HKT).minute
                    temp_list_earliest_sunset[5]=ti.astimezone(HKT).second  
temp_list_earliest_sunset[1]='Earliest sunset of the year'
temp_list_earliest_sunset[0]='全年最早日落'
temp_list_earliest_sunset[4]=''
temp_list_earliest_sunset[5]=1           
print(temp_list_earliest_sunset)
sunrise_sun.append(temp_list_earliest_sunset)