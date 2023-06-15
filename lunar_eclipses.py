# this avdance lunar eclipse will consider the size of earth's shadow during each eclipse

from skyfield import eclipselib
from skyfield.api import Star
from main import *
import numpy as np
from skyfield.searchlib import find_minima
# t0 = ts.utc(2021, 1, 1)
# t1 = ts.utc(2022, 5, 31)
t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)
Earth_radius=6378.1366
k_IAU=0.2725076
moon_radius_km=Earth_radius*k_IAU
# mean = 1737.4
# equatorial = 1738.1
# Polar=1736
list_lunar_eclipses=[]
lunar_eclipses_counter=0

# The following functions find the separation between the center of the moon and the limb of Earth's urmbra, so as to deduce the time of each contact.

def limb_separation_at_partial_eclipse(t_limb_partial):
    # e_HKO = (earth + HKO).at(t_limb_partial) # Observe from HKO
    e = earth.at(t_limb_partial) # Observe from earth center
    s = e.observe(sun).apparent()
    m = e.observe(moon).apparent()
    # m_HKO = e_HKO.observe(moon).apparent()
    moon_distance=m.distance().km
    moon_angular_radius_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)
    # moon_angular_radius_degrees=(details['moon_radius_radians'][0]*180/np.pi)
    umbra_radius_deg=details['umbra_radius_radians'][lunar_eclipses_counter]*180/np.pi
    return abs(180-umbra_radius_deg-moon_angular_radius_degrees-s.separation_from(m).degrees)

def limb_separation_at_total_eclipse(t_limb_total):
    # e_HKO = (earth + HKO).at(t_limb_total) # Observe from HKO
    e = earth.at(t_limb_total) # Observe from earth center
    s = e.observe(sun).apparent()
    m = e.observe(moon).apparent()
    # m_HKO = e_HKO.observe(moon).apparent()
    moon_distance=m.distance().km
    moon_angular_radius_degrees=np.arctan(moon_radius_km/moon_distance)*(180/np.pi)
    # moon_angular_radius_degrees=(details['moon_radius_radians'][0]*180/np.pi)
    umbra_radius_deg=details['umbra_radius_radians'][lunar_eclipses_counter]*180/np.pi
    return abs(180-umbra_radius_deg+moon_angular_radius_degrees-s.separation_from(m).degrees)

limb_separation_at_partial_eclipse.step_days = 1
limb_separation_at_total_eclipse.step_days = 1

for yi, ti in zip(y, t):
    
    # A list of maximum is created here from eclipselib----------------------------------------
    temp_list_lunar_eclipses=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
    temp_list_lunar_eclipses[2]=ti.astimezone(HKT).date()
    temp_list_lunar_eclipses[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
    temp_list_lunar_eclipses[4]=''
    temp_list_lunar_eclipses[1]=eclipselib.LUNAR_ECLIPSES[yi] + " Lunar Eclipse (Maximum)"
    # umbra_radius_deg=details['umbra_radius_radians'][lunar_eclipses_counter]*180/np.pi
    if yi==0:
        temp_list_lunar_eclipses[0]='半影月食 (食甚)'
    if yi==1:
        temp_list_lunar_eclipses[0]='月偏食 (食甚)'
        # Two of more lists of partial eclipse phases are created here from calcuation-------------
    
        limb_separation_times_partial_eclipse, limb_separation_partial_eclipse = find_minima(ti-1, ti+1, limb_separation_at_partial_eclipse)
        try:
            zipb_partial, zipc_partial=zip(*[i for i in zip(limb_separation_times_partial_eclipse, limb_separation_partial_eclipse) if i[1]<0.01])
            partial_list=[0,1]*int(len(zipc_partial)/2)
            
            for t_limb_partial, limb_separation_deg, partial in zip(zipb_partial, zipc_partial, partial_list):
                
                e_HKO = (earth + HKO).at(t_limb_partial) # Observe from HKO
                m_alt_partial = e_HKO.observe(moon).apparent().altaz()[0].degrees
            # if m_alt_partial >0.5:
                temp_list_lunar_partial_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
                temp_list_lunar_partial_eclipse[2]=t_limb_partial.astimezone(HKT).date()
                temp_list_lunar_partial_eclipse[3]=(float(t_limb_partial.astimezone(HKT).time().hour)+float(t_limb_partial.astimezone(HKT).time().minute)/60+float(t_limb_partial.astimezone(HKT).time().second)/3600)/24
                temp_list_lunar_partial_eclipse[4]=''

                if partial == 0:
                    temp_list_lunar_partial_eclipse[0]="月偏食開始"
                    temp_list_lunar_partial_eclipse[1]="Partial Lunar Eclipse Starts"
                if partial == 1:
                    temp_list_lunar_partial_eclipse[0]="月偏食結束"
                    temp_list_lunar_partial_eclipse[1]="Partial Lunar Eclipse Ends"
                if m_alt_partial <0:
                    temp_list_lunar_partial_eclipse[4]='香港不可見'
                    temp_list_lunar_partial_eclipse[5]='1' #change this number if user want to degarde eclipses/phases that are not visible in Hong Kong.
                else:
                    temp_list_lunar_partial_eclipse[4]=''
                    temp_list_lunar_partial_eclipse[5]='1'            
                print(temp_list_lunar_partial_eclipse)
                list_lunar_eclipses.append(temp_list_lunar_partial_eclipse)   
        except:
            pass
        # Two of more lists of partial eclipse phases are created here from calcuation-------------        
        
        
    if yi==2:
        temp_list_lunar_eclipses[0]='月全食 (食甚)'
        # Phases of partial eclipse phases will be created first-----------------------------------
    
        limb_separation_times_partial_eclipse, limb_separation_partial_eclipse = find_minima(ti-1, ti+1, limb_separation_at_partial_eclipse)
        try:
            zipb_partial, zipc_partial=zip(*[i for i in zip(limb_separation_times_partial_eclipse, limb_separation_partial_eclipse) if i[1]<0.01])
            partial_list=[0,1]*int(len(zipc_partial)/2)
            
            for t_limb_partial, limb_separation_deg, partial in zip(zipb_partial, zipc_partial, partial_list):
                
                e_HKO = (earth + HKO).at(t_limb_partial) # Observe from HKO
                m_alt_partial = e_HKO.observe(moon).apparent().altaz()[0].degrees
            # if m_alt_partial >0.5:
                temp_list_lunar_partial_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
                temp_list_lunar_partial_eclipse[2]=t_limb_partial.astimezone(HKT).date()
                temp_list_lunar_partial_eclipse[3]=(float(t_limb_partial.astimezone(HKT).time().hour)+float(t_limb_partial.astimezone(HKT).time().minute)/60+float(t_limb_partial.astimezone(HKT).time().second)/3600)/24
                temp_list_lunar_partial_eclipse[4]=''

                if partial == 0:
                    temp_list_lunar_partial_eclipse[0]="月偏食開始"
                    temp_list_lunar_partial_eclipse[1]="Partial Lunar Eclipse Starts"
                if partial == 1:
                    temp_list_lunar_partial_eclipse[0]="月偏食結束"
                    temp_list_lunar_partial_eclipse[1]="Partial Lunar Eclipse Ends"
                if m_alt_partial <0:
                    temp_list_lunar_partial_eclipse[4]='香港不可見'
                    temp_list_lunar_partial_eclipse[5]='1' #change this number if user want to degarde eclipses/phases that are not visible in Hong Kong.
                else:
                    temp_list_lunar_partial_eclipse[4]=''
                    temp_list_lunar_partial_eclipse[5]='1'            
                print(temp_list_lunar_partial_eclipse)
                list_lunar_eclipses.append(temp_list_lunar_partial_eclipse)   
        except:
            pass
        # Phases of partial eclipse phases will be created first-----------------------------------
        # Two of more lists of total eclipse phases are created here from calcuation---------------
    
        limb_separation_times_total_eclipse, limb_separation_total_eclipse = find_minima(ti-1, ti+1, limb_separation_at_total_eclipse)
        try:
            zipb_total, zipc_total=zip(*[i for i in zip(limb_separation_times_total_eclipse, limb_separation_total_eclipse) if i[1]<0.1])  
            total_list=[0,1]*int(len(zipc_total)/2)
            for t_limb_total, limb_separation_deg, total in zip(zipb_total, zipc_total, total_list):
                
                e_HKO = (earth + HKO).at(t_limb_total) # Observe from HKO
                m_alt_total = e_HKO.observe(moon).apparent().altaz()[0].degrees
                temp_list_lunar_total_eclipse=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
                temp_list_lunar_total_eclipse[2]=t_limb_total.astimezone(HKT).date()
                temp_list_lunar_total_eclipse[3]=(float(t_limb_total.astimezone(HKT).time().hour)+float(t_limb_total.astimezone(HKT).time().minute)/60+float(t_limb_total.astimezone(HKT).time().second)/3600)/24
                if total == 0:
                    temp_list_lunar_total_eclipse[0]="月全食開始"
                    temp_list_lunar_total_eclipse[1]="Total Lunar Eclipse Starts"
                if total == 1:
                    temp_list_lunar_total_eclipse[0]="月全食結束"
                    temp_list_lunar_total_eclipse[1]="Total Lunar Eclipse Ends"
                if m_alt_total <0:
                    temp_list_lunar_total_eclipse[4]='香港不可見'
                    temp_list_lunar_total_eclipse[5]='1' #change this number if user want to degarde eclipses/phases that are not visible in Hong Kong.
                else:
                    temp_list_lunar_total_eclipse[4]=''
                    temp_list_lunar_total_eclipse[5]='1'            
                print(temp_list_lunar_total_eclipse)
                list_lunar_eclipses.append(temp_list_lunar_total_eclipse)   
        except:
            pass
        # Two of more lists of total eclipse phases are created here from calcuation---------------        
        
        
    e_HKO = (earth + HKO).at(ti) # Observe from HKO
    m_alt_max = e_HKO.observe(moon).apparent().altaz()[0].degrees
    if m_alt_max >0.5:
        temp_list_lunar_eclipses[5]='1'
    else:
        temp_list_lunar_eclipses[5]='1'
        temp_list_lunar_eclipses[4]='香港不可見'
    list_lunar_eclipses.append(temp_list_lunar_eclipses)
    print(temp_list_lunar_eclipses)
    # A list of maximum is created here from eclipselib----------------------------------------
        
    lunar_eclipses_counter=lunar_eclipses_counter+1
    # print(lunar_eclipses_counter)
lunar_eclipses_counter=0
