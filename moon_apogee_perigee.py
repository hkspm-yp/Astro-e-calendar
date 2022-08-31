from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima, find_minima
from main import *
from pytz import timezone


def moon_apogee(t):
    e = earth.at(t)
    md = e.observe(moon).apparent()
    return md.distance().km

# moon_close(t)

moon_apogee.step_days = 2.0

moon_apogee_times, moon_apogee_s = find_maxima(t0, t1, moon_apogee)

list_moon_apogee=[]
for t, moon_apogee_distance in zip(moon_apogee_times, moon_apogee_s):

    temp_list_moon_apogee=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_moon_apogee[2]=t.astimezone(HKT).date()
    temp_list_moon_apogee[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_moon_apogee[4]=''
    temp_list_moon_apogee[1]='Moon at apogee (' + str(int(moon_apogee_distance)) + 'km)'
    temp_list_moon_apogee[0]='月球過遠地點 (' + str(int(moon_apogee_distance)) + '公里)'
    temp_list_moon_apogee[5]=3
    list_moon_apogee.append(temp_list_moon_apogee)
    print(temp_list_moon_apogee)

# -----------------------------------
def moon_perigee(t):
    e = earth.at(t)
    md = e.observe(moon).apparent()
    return md.distance().km

# moon_close(t)

moon_perigee.step_days = 2.0

moon_perigee_times, moon_perigee_s = find_minima(t0, t1, moon_perigee)

list_moon_perigee=[]
for t, moon_perigee_distance in zip(moon_perigee_times, moon_perigee_s):

    temp_list_moon_perigee=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_moon_perigee[2]=t.astimezone(HKT).date()
    temp_list_moon_perigee[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_moon_perigee[4]=''
    temp_list_moon_perigee[1]='Moon at perigee (' + str(int(moon_perigee_distance)) + 'km)'
    temp_list_moon_perigee[0]='月球過近地點 (' + str(int(moon_perigee_distance)) + '公里)'
    temp_list_moon_perigee[5]=3
    list_moon_perigee.append(temp_list_moon_perigee)
    print(temp_list_moon_perigee)