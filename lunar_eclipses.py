from skyfield import eclipselib
from main import *
# t0 = ts.utc(2020, 1, 1)
# t1 = ts.utc(2022, 12, 31)
t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)

list_lunar_eclipses=[]
for yi, ti in zip(y, t):
    temp_list_lunar_eclipses=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_lunar_eclipses[2]=ti.astimezone(HKT).date()
    temp_list_lunar_eclipses[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
    temp_list_lunar_eclipses[4]=''
    temp_list_lunar_eclipses[1]=eclipselib.LUNAR_ECLIPSES[yi] + " Lunar Eclipse"
    temp_list_lunar_eclipses[5]='1/香港不可見'
    if yi==0:
        temp_list_lunar_eclipses[0]='半影月食'
    if yi==1:
        temp_list_lunar_eclipses[0]='月偏食'
    if yi==2:
        temp_list_lunar_eclipses[0]='月全食'
    list_lunar_eclipses.append(temp_list_lunar_eclipses)
    print(temp_list_lunar_eclipses)