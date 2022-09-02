from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima, find_minima
from main import *
from pytz import timezone


def earth_aphelion(t):
    e = earth.at(t)
    md = e.observe(sun).apparent()
    return md.distance().km

# earth_close(t)

earth_aphelion.step_days = 15.0
earth_aphelion.step_days = 15.0

earth_aphelion_times, earth_aphelion_s = find_maxima(t0, t1, earth_aphelion)

list_earth_aphelion=[]
for t, earth_aphelion_distance in zip(earth_aphelion_times, earth_aphelion_s):

    temp_list_earth_aphelion=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_earth_aphelion[2]=t.astimezone(HKT).date()
    temp_list_earth_aphelion[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_earth_aphelion[4]=str(int(earth_aphelion_distance)) + 'km'
    temp_list_earth_aphelion[1]='Earth at aphelion'
    temp_list_earth_aphelion[0]='地球過遠日點'
    temp_list_earth_aphelion[5]=3
    list_earth_aphelion.append(temp_list_earth_aphelion)
    print(temp_list_earth_aphelion)

# -----------------------------------
def earth_perihelion(t):
    e = earth.at(t)
    md = e.observe(sun).apparent()
    return md.distance().km

# earth_close(t)

earth_perihelion.step_days = 15.0
earth_perihelion.step_days = 15.0

earth_perihelion_times, earth_perihelion_s = find_minima(t0, t1, earth_perihelion)

list_earth_perihelion=[]
for t, earth_perihelion_distance in zip(earth_perihelion_times, earth_perihelion_s):

    temp_list_earth_perihelion=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_earth_perihelion[2]=t.astimezone(HKT).date()
    temp_list_earth_perihelion[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_earth_perihelion[4]=str(int(earth_perihelion_distance)) + 'km'
    temp_list_earth_perihelion[1]='Earth at perihelion'
    temp_list_earth_perihelion[0]='地球過近日點'
    temp_list_earth_perihelion[5]=3
    list_earth_perihelion.append(temp_list_earth_perihelion)
    print(temp_list_earth_perihelion)