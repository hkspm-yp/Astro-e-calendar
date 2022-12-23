from main import *

temp_list_twilight=['0','0','0','0','0','0']
list_twilight=[]

# t0 = ts.utc(year, 1, 1) - 1/3
# t1 = ts.utc(year, 12, 31) - 1/3

t, y = almanac.find_discrete(t0, t1, almanac.dark_twilight_day(eph, HKO))
y_number=len(y)
y=[1,2,3,4,5,6,7,8]*int(y_number/8)

for yi, ti in zip(y, t):
    if yi==1:
        temp_list_twilight=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_twilight[0]='天文曙光開始'
        temp_list_twilight[1]='Astronomical twilight starts'
        temp_list_twilight[2]=ti.astimezone(HKT).date()
        temp_list_twilight[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
        # temp_list_twilight[3]=ti.astimezone(HKT).time().isoformat("milliseconds")
        temp_list_twilight[4]=''
        temp_list_twilight[5]=''
        
        print(temp_list_twilight)
        list_twilight.append(temp_list_twilight)


    if yi==8:
        temp_list_twilight=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_twilight[0]='天文暮光結束'
        temp_list_twilight[1]='Astronomical twilight ends'
        temp_list_twilight[2]=ti.astimezone(HKT).date()
        temp_list_twilight[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
        # temp_list_twilight[3]=ti.astimezone(HKT).time().isoformat("milliseconds")
        temp_list_twilight[4]=''
        temp_list_twilight[5]=''        
        print(temp_list_twilight)
        list_twilight.append(temp_list_twilight)

# yi==2 -> Nautical twilight starts
# yi==3 -> Civil twilight starts
# yi==4 -> Day starts
# yi==5 -> Day ends
# yi==6 -> Civil twilight ends
# yi==7 -> Nautical twilight ends