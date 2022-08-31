from skyfield import api
from skyfield import almanac
import pandas as pd

from pytz import timezone

ts = api.load.timescale()
eph = api.load('de440.bsp')

sun = eph['sun']
mercury = eph['mercury']
venus = eph['venus']
earth = eph['earth']
moon = eph['moon']
mars = eph['mars barycenter']
jupiter = eph['jupiter barycenter']
saturn = eph['saturn barycenter']
uranus = eph['uranus barycenter']
neptune = eph['neptune barycenter']
pluto = eph['pluto barycenter']

HKT = timezone('Asia/Hong_Kong')
t0 = ts.utc(2021, 1, 1) - 1/3
t1 = ts.utc(2021, 12, 31) - 1/3

# from opposition import*
list0=[['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']]

#moon_phase()
if __name__ == '__main__':
    from season_events import *    
    from moon_phase import *    
    from opposition import *    
    from elongations import *    
    from moon_apogee_perigee import *    
    from earth_apohelion_perihelion import *    
    from lunar_conjunctions import *    
    from planetary_conjunctions import *
    # from sunrise_sunset import *
    list0.extend(
        list_SEASON_EVENTS +
        list_moon_phases + 
        list_oppositions_conjunctions + 
        list_elongations + 
        list_moon_apogee +
        list_moon_perigee +    
        list_earth_aphelion +
        list_earth_perihelion +
        list_lunar_conjunctions +
        list_planetary_conjunctions
        # sunrise_sun
        )
    #df[list_SEASON_EVENTS]=list0
    pd.DataFrame(list0).to_excel('output.xlsx', header=False, index=False)
    print('output.xlsx is saved.')