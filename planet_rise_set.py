from main import *

planet_list=[mercury, venus, mars, jupiter, saturn]

planet_name_list_eng=['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
planet_name_list_chi=['水星', '金星', '火星', '木星', '土星']

temp_list_rising_setting=['0','0','0','0','0','0']
list_rising_setting=[]

for i in range(len(planet_list)):
    f = almanac.risings_and_settings(eph, planet_list[i], HKO)
    t, y = almanac.find_discrete(t0, t1, f)
    for yi, ti in zip(y, t):
        if yi==1:
            temp_list_rising_setting=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_rising_setting[0]=planet_name_list_chi[i] + '出'
            temp_list_rising_setting[1]=planet_name_list_eng[i] + ' rises'
            temp_list_rising_setting[2]=ti.astimezone(HKT).date()
            temp_list_rising_setting[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
            # temp_list_rising_setting[3]=ti.astimezone(HKT).time().isoformat("milliseconds")
            temp_list_rising_setting[4]=''
            temp_list_rising_setting[5]=''
            
            print(temp_list_rising_setting)
            list_rising_setting.append(temp_list_rising_setting)
    
        if yi==0:
            temp_list_rising_setting=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_rising_setting[0]=planet_name_list_chi[i] + '落'
            temp_list_rising_setting[1]=planet_name_list_eng[i] +' sets'
            temp_list_rising_setting[2]=ti.astimezone(HKT).date()
            temp_list_rising_setting[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
            # temp_list_rising_setting[3]=ti.astimezone(HKT).time().isoformat("milliseconds")
            temp_list_rising_setting[4]=''
            temp_list_rising_setting[5]=''
            
            print(temp_list_rising_setting)
            list_rising_setting.append(temp_list_rising_setting)
        