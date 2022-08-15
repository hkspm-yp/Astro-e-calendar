from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima, find_minima
from main import *
from pytz import timezone


def moon_apogee(t):
    e = earth.at(t)
    md = e.observe(moon).apparent()
    return md.distance().km

# moon_close(t)

moon_apogee.step_days = 15.0
moon_apogee.step_days = 15.0

moon_apogee_times, moon_apogee_s = find_maxima(t0, t1, moon_apogee)

list_moon_apogee=[]
for t, moon_apogee_distance in zip(moon_apogee_times, moon_apogee_s):

    temp_list_moon_apogee=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
    temp_list_moon_apogee[0]=t.astimezone(HKT).year
    temp_list_moon_apogee[1]=t.astimezone(HKT).month
    temp_list_moon_apogee[2]=t.astimezone(HKT).day
    temp_list_moon_apogee[3]=t.astimezone(HKT).hour
    temp_list_moon_apogee[4]=t.astimezone(HKT).minute
    temp_list_moon_apogee[5]=int(t.astimezone(HKT).second)
    temp_list_moon_apogee[6]='Moon at apogee (' + str(int(moon_apogee_distance)) + 'km)'
    temp_list_moon_apogee[7]='月球過遠地點 (' + str(int(moon_apogee_distance)) + '公里)'
    list_moon_apogee.append(temp_list_moon_apogee)
    print(temp_list_moon_apogee)

# -----------------------------------
def moon_perigee(t):
    e = earth.at(t)
    md = e.observe(moon).apparent()
    return md.distance().km

# moon_close(t)

moon_perigee.step_days = 15.0
moon_perigee.step_days = 15.0

moon_perigee_times, moon_perigee_s = find_minima(t0, t1, moon_perigee)

list_moon_perigee=[]
for t, moon_perigee_distance in zip(moon_perigee_times, moon_perigee_s):

    temp_list_moon_perigee=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
    temp_list_moon_perigee[0]=t.astimezone(HKT).year
    temp_list_moon_perigee[1]=t.astimezone(HKT).month
    temp_list_moon_perigee[2]=t.astimezone(HKT).day
    temp_list_moon_perigee[3]=t.astimezone(HKT).hour
    temp_list_moon_perigee[4]=t.astimezone(HKT).minute
    temp_list_moon_perigee[5]=int(t.astimezone(HKT).second)
    temp_list_moon_perigee[6]='Moon at perigee (' + str(int(moon_perigee_distance)) + 'km)'
    temp_list_moon_perigee[7]='月球過近地點 (' + str(int(moon_perigee_distance)) + '公里)'
    list_moon_perigee.append(temp_list_moon_perigee)
    print(temp_list_moon_perigee)