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
year = 2023
t0 = ts.utc(year, 1, 1) - 1/3
t1 = ts.utc(year, 12, 31) - 1/3

list0=[['1. Chin. Title', '2. Eng. Title','Date','HKT','Remark','Level (highest=1)']]

if __name__ == '__main__':
    from season_events import *    
    from moon_phase import *    
    from opposition import *    
    from elongations import *    
    from moon_apogee_perigee import *    
    from earth_apohelion_perihelion import *    
    from lunar_appulse import *    
    from planetary_appulse import *
    from stars_lunar_appulse import *
    from sunrise_sunset import *
    from meteor_shower import*
    from lunar_conjunctions_RA import *
    from lunar_eclipses import *
    from planetary_conjunctions_RA import *
    from stars_lunar_conjunctions_RA import *
    list0.extend(
        list_SEASON_EVENTS +
        list_moon_phases +
        list_oppositions_conjunctions + 
        list_elongations + 
        list_moon_apogee +
        list_moon_perigee +    
        list_earth_aphelion +
        list_earth_perihelion +
        list_lunar_appulse +
        list_planetary_appulse +
        list_stars_appulse +
        sunrise_sun + 
        list_meteor_shower +
        list_lunar_conjunctions +
        list_lunar_eclipses +
        list_planetary_conjunctions +
        list_stars_conjunctions
        )
    pd.DataFrame(list0).to_excel('output'+ str(year) +'.xlsx', header=False, index=False)
    print('output'+ str(year) +'.xlsx is saved.')