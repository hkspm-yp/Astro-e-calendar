from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_maxima
from main import *
from pytz import timezone

def venus_elongation_at(t):
    e = earth.at(t)
    s = e.observe(sun).apparent()
    v = e.observe(venus).apparent()
    return s.separation_from(v).degrees

def mercury_elongation_at(t):
    e = earth.at(t)
    s = e.observe(sun).apparent()
    m = e.observe(mercury).apparent()
    return s.separation_from(m).degrees

venus_elongation_at.step_days = 15.0
mercury_elongation_at.step_days = 15.0

Venus_times, Venus_elongations = find_maxima(t0, t1, venus_elongation_at)
Mercury_times, Mercury_elongations = find_maxima(t0, t1, mercury_elongation_at)
list_elongations=[]
for t, Venus_elongation_degrees in zip(Venus_times, Venus_elongations):
    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
    _, vlon, _ = e.observe(venus).apparent().frame_latlon(ecliptic_frame)
    venus_is_east = (vlon.degrees - slon.degrees) % 360.0 < 180.0
    Venus_direction = 'Eastern elongation of Venus' if venus_is_east else 'Western elongation of Venus'
    Venus_direction_chi = '金星東大距' if venus_is_east else '金星西大距'        
    #print('{}  {:4.1f}° {} elongation'.format(
    #    t.astimezone(HKT)_strftime(), elongation_degrees, direction))
    temp_list_elongations=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_elongations[2]=t.astimezone(HKT).date()
    temp_list_elongations[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_elongations[4]=''
    temp_list_elongations[1]=Venus_direction + ' (' + str(int(Venus_elongation_degrees)) +'°)'
    temp_list_elongations[0]=Venus_direction_chi + ' (' + str(int(Venus_elongation_degrees)) +'°)'
    temp_list_elongations[5]=1
    list_elongations.append(temp_list_elongations)    
    print(temp_list_elongations)

for t, Mercury_elongation_degrees in zip(Mercury_times, Mercury_elongations):
    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
    _, mlon, _ = e.observe(mercury).apparent().frame_latlon(ecliptic_frame)     
    Mercury_is_east = (mlon.degrees - slon.degrees) % 360.0 < 180.0
    Mercury_direction = 'Eastern elongation of Mercury' if Mercury_is_east else 'Western elongation of Mercury'
    Mercury_direction_chi = '水星東大距' if Mercury_is_east else '水星西大距'
    #print('{}  {:4.1f}° {} elongation'.format(
    #    t.astimezone(HKT)_strftime(), elongation_degrees, direction))
    temp_list_elongations=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_elongations[2]=t.astimezone(HKT).date()
    temp_list_elongations[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
    temp_list_elongations[4]=''
    temp_list_elongations[1]=Mercury_direction + ' (' + str(int(Mercury_elongation_degrees)) +'°)'
    temp_list_elongations[0]=Mercury_direction_chi + ' (' + str(int(Mercury_elongation_degrees)) +'°)'
    temp_list_elongations[5]=1
    list_elongations.append(temp_list_elongations)
    print(temp_list_elongations)