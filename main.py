from skyfield import api
from skyfield import almanac
import pandas as pd
from skyfield.api import wgs84
from skyfield.api import N, S, E, W
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
HKO = api.wgs84.latlon(+22.30202, +114.17433)

list0=[['1. Chin. Title', '2. Eng. Title','Date','HKT','Remark','Level (highest=1)']]
df_google= pd.DataFrame()
if __name__ == '__main__':
    # from season_events import *    
    # from moon_phase import *
    # from opposition import *    
    # from elongations import *    
    # from moon_apogee_perigee import *    
    # from earth_apohelion_perihelion import *    
    # from lunar_appulse import *    
    # from planetary_appulse import *
    # from stars_lunar_appulse import *
    # from earliest_latest_sunrise_sunset import *
    # from lunar_eclipses import *    
    # from lunar_conjunctions_RA import *
    # from planetary_conjunctions_RA import *
    # from planetary_conjunctions_elong import *
    # from stars_lunar_conjunctions_RA import *
    # from meteor_shower import*
    
    from all_year_sunrise_sunset import*
    from twilight import*
    from planet_rise_set import*
    list0.extend(
        # list_meteor_shower +
        # list_SEASON_EVENTS 
        # list_moon_phases
        # list_oppositions_conjunctions +
        # list_elongations + 
        # list_moon_apogee +
        # list_moon_perigee +    
        # list_earth_aphelion +
        # list_earth_perihelion +
        # list_lunar_appulse +
        # list_planetary_appulse +
        # list_stars_appulse +
        # list_sunrise_sunset + 
        # list_lunar_eclipses +
        # list_lunar_conjunctions_RA +
        # list_planetary_conjunctions_RA +
        # list_planetary_conjunctions_elong +
        # list_stars_conjunctions_RA +
        
        list_sunrise +        
        list_sunset +
        list_twilight +
        list_rising_setting
        )
    pd.DataFrame(list0).to_excel('Astro E-calendar '+ str(year) +' raw.xlsx', header=False, index=False)
    print('Astro E-calendar '+ str(year) +' raw.xlsx is saved. Please input solar eclipse information and update the meteor shower information.')

    # df_google[1] = pd.DataFrame(list0)[0]+ ' ' + pd.DataFrame(list0)[1]
    # df_google[2] = pd.DataFrame(list0)[4]
    # df_google[3] = pd.DataFrame(list0)[2]
    # df_google[4] = pd.DataFrame(list0)[3]
    # df_google[5] = pd.DataFrame(list0)[2] 
    # df_google[6] = pd.DataFrame(list0)[3]
    # df_google[1][0]='Subject'
    # df_google[2][0]='Description'
    # df_google[3][0]='Start Date'    
    # df_google[4][0]='Start Time'
    # df_google[5][0]='End Date'    
    # df_google[6][0]='End Time'
    # df_google.to_csv('Astro E-calendar_for google calendar '+ str(year) +' raw.csv', encoding='utf-8_sig', header=False, index=False)
    # print('Astro E-calendar for google calendar '+ str(year) +' raw.csv is saved. Please input solar eclipse information and update the meteor shower information.')