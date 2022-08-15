from datetime import datetime
from main import *
bluffton = api.wgs84.latlon(+22.12, +114.22)
# t0 = ts.utc(2021, 5, 12, 4)
# t1 = ts.utc(2021, 7, 23, 4)
t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))
temp_list_sunrise_sunset=['0', '0','0','0','0','0','0','0']
latest_sunrise=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
for yi, ti in zip(y, t):
    if yi==0:
        if  ti.astimezone(HKT).month==6:
            temp_list_sunrise_sunset[0]=ti.astimezone(HKT).year
            temp_list_sunrise_sunset[1]=ti.astimezone(HKT).month
            # temp_list_sunrise_sunset[2]=ti.astimezone(HKT).day
            # temp_list_sunrise_sunset[3]=ti.astimezone(HKT).hour
            # temp_list_sunrise_sunset[4]=ti.astimezone(HKT).minute
            # temp_list_sunrise_sunset[5]=ti.astimezone(HKT).second
            temp_list_sunrise_sunset[6]='Sunset'
            temp_list_sunrise_sunset[7]='日落'

            
            if int(ti.astimezone(HKT).minute)>= int(temp_list_sunrise_sunset[4]):
                if float(ti.astimezone(HKT).second)>= float(temp_list_sunrise_sunset[5]):
                    temp_list_sunrise_sunset[2]=ti.astimezone(HKT).day
                    temp_list_sunrise_sunset[3]=ti.astimezone(HKT).hour
                    temp_list_sunrise_sunset[4]=ti.astimezone(HKT).minute
                    temp_list_sunrise_sunset[5]=ti.astimezone(HKT).second
                    print(temp_list_sunrise_sunset)
                    

#             latest_sunrise=temp_list_sunrise_sunset
# print(latest_sunrise)