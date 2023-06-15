from skyfield import api
from skyfield.api import wgs84
from skyfield.searchlib import find_minima
from pytz import timezone
import numpy as np
import time
from main import *

t0 = ts.utc(2011, 4, 1) - 1/3
t1 = ts.utc(2013, 4, 31) - 1/3
sun_radius_km=695700
# At 535.7 nm, Rs=696134 (PICARD mission, 2018)
# At 607.1 nm, Rs=696156
# Nominal solar radius, Rs=695700 (IAU, 2015)
# Canonical value, Rs=695996.7
Earth_radius=6378.1366
k_IAU=0.2725076
moon_radius_km=Earth_radius*k_IAU

temp_list_solar_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
list_solar_eclipses=[]

# The first function calcuates the times of maximum eclipse by finding the closing angular separation between the sun and the moon.

def separation_at(t):
    e = (earth + HKO).at(t) # Observe from HKO
    m = e.observe(moon).apparent()
    s = e.observe(sun).apparent()
    return s.separation_from(m).degrees
separation_at.step_days = 5
separation_times, separation = find_minima(t0, t1, separation_at)

for t, separation_deg in zip(separation_times, separation):
    
    e = (earth + HKO).at(t) # Observe from HKO
    m = e.observe(moon).apparent()
    s = e.observe(sun).apparent()
    sun_moon_separation=s.separation_from(m).degrees
    sun_distance=s.distance().km
    moon_distance=m.distance().km    
    sun_angular_diameter_degrees=np.arctan(sun_radius_km/sun_distance)*(180/np.pi)*2
    moon_angular_diameter_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)*2
    mag=round(((sun_angular_diameter_degrees+moon_angular_diameter_degrees)/2-separation_deg)/sun_angular_diameter_degrees, 4)
    if separation_deg<(sun_angular_diameter_degrees+moon_angular_diameter_degrees)/2 and e.observe(sun).apparent().altaz()[0].degrees >-10:
        temp_list_solar_max_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']       
        temp_list_solar_max_eclipse[0]="日食食甚"
        temp_list_solar_max_eclipse[1]="Solar Eclipse (Maximum)"  
        temp_list_solar_max_eclipse[2]=t.astimezone(HKT).date()
        temp_list_solar_max_eclipse[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second+t.astimezone(HKT).time().microsecond/1000000)/3600)/24
        temp_list_solar_max_eclipse[4]='食分 Magnitude ' + str(mag)
        temp_list_solar_max_eclipse[5]='1'
        print(temp_list_solar_max_eclipse)
        list_solar_eclipses.append(temp_list_solar_max_eclipse)      

# The second function calcuates the times of contact between the solar limb and lunar limb.

def limb_separation_at(t_limb):
    e = (earth + HKO).at(t_limb) # Observe from HKO
    m = e.observe(moon).apparent()
    s = e.observe(sun).apparent()
    sun_distance=s.distance().km
    moon_distance=m.distance().km
    sun_angular_diameter_degrees=np.arctan(sun_radius_km/sun_distance)*(180/np.pi)*2
    moon_angular_diameter_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)*2
    return abs(((sun_angular_diameter_degrees+moon_angular_diameter_degrees)/2)-s.separation_from(m).degrees)
limb_separation_at.step_days = 5
limb_separation_times, limb_separation = find_minima(t0, t1, limb_separation_at)

zipb, zipc=zip(*[i for i in zip(limb_separation_times, limb_separation) if i[1]<0.5])
for t_limb, limb_separation_deg in zip(zipb, zipc):
    
    e = (earth + HKO).at(t_limb) # Observe from HKO
    s_alt = e.observe(sun).apparent().altaz()[0].degrees
    if s_alt >-10:
        
        if t_limb.astimezone(HKT).date() != temp_list_solar_eclipse[2]:
            temp_list_solar_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_solar_eclipse[2]=t_limb.astimezone(HKT).date()
            temp_list_solar_eclipse[3]=(float(t_limb.astimezone(HKT).time().hour)+float(t_limb.astimezone(HKT).time().minute)/60+float(t_limb.astimezone(HKT).time().second+t_limb.astimezone(HKT).time().microsecond/1000000)/3600)/24
            temp_list_solar_eclipse[4]=''
            temp_list_solar_eclipse[0]="日食初虧"
            temp_list_solar_eclipse[1]="Solar Eclipse Starts"
            temp_list_solar_eclipse[5]='1'
        else:
            print(temp_list_solar_eclipse)
            list_solar_eclipses.append(temp_list_solar_eclipse)
            temp_list_solar_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_solar_eclipse[2]=t_limb.astimezone(HKT).date()
            temp_list_solar_eclipse[3]=(float(t_limb.astimezone(HKT).time().hour)+float(t_limb.astimezone(HKT).time().minute)/60+float(t_limb.astimezone(HKT).time().second+t_limb.astimezone(HKT).time().microsecond/1000000)/3600)/24
            temp_list_solar_eclipse[4]=''
            temp_list_solar_eclipse[0]="日食復圓"
            temp_list_solar_eclipse[1]="Solar Eclipse Ends"
            temp_list_solar_eclipse[5]='1'
            print(temp_list_solar_eclipse)
            list_solar_eclipses.append(temp_list_solar_eclipse)   