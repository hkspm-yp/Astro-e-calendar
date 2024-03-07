from skyfield.api import Star, load
# planets = load('de440.bsp')
# earth = planets['earth']
# ts = load.timescale()
# t = ts.now()
# astrometric = earth.at(t).observe(barnard)
# ra, dec, distance = astrometric.radec()
# print(ra)
# print(dec)

from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

name_list_chi=['角宿一合月', '軒轅十四合月', '心宿二合月', '畢宿五合月', '北河三合月']
name_list_eng=['Spica-Moon Conjunction',
               'Regulus-Moon Conjunction',
               'Antares-Moon Conjunction',
               'Aldebaran-Moon Conjunction',
               'Pollux-Moon Conjunction',]

#The Hipparcos and Tycho Catalogues (ESA 1997)
Spica = Star(ra_hours=(13, 25, 11.5792824),
             dec_degrees=(-11, 9, 40.759313),             
             ra_mas_per_year=-42.50,
             dec_mas_per_year=-31.73,
             parallax_mas=12.44)

Regulus = Star(ra_hours=(10, 8, 22.3106646),
               dec_degrees=(11, 58, 1.945428),             
               ra_mas_per_year=-249.40,
               dec_mas_per_year=4.91,
               parallax_mas=42.09)


Antares = Star(ra_hours=(16, 29, 24.4609111),
               dec_degrees=(-26, 25, 55.208975),             
               ra_mas_per_year=-10.16	,
               dec_mas_per_year=-23.21,
               parallax_mas=5.40)

Aldebaran = Star(ra_hours=(4, 35, 55.2386644),
                 dec_degrees=(16, 30, 33.485004),             
                 ra_mas_per_year=62.78,
                 dec_mas_per_year=-189.36,
                 parallax_mas=50.09	)

Pollux = Star(ra_hours=(7, 45, 18.9503586), 
              dec_degrees=(28, 1, 34.315015),             
              ra_mas_per_year=-625.69,
              dec_mas_per_year=-45.95,
              parallax_mas=96.74)

stars_list = [Spica, Regulus, Antares, Aldebaran, Pollux]
list_stars_conjunctions_RA = []


for i in range(len(stars_list)):
    def separation_at(t):
        e = earth.at(t)
        s = e.observe(moon).apparent()
        m = e.observe(stars_list[i]).apparent()
        sRa, _, _ = s.radec(epoch = 'date')
        mRa, _, _ = m.radec(epoch = 'date')
        return abs(sRa.hours - mRa.hours)

    separation_at.step_days = 14.5
    
    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        if separation_degrees < 0.1:
            temp_list_stars_conjunctions_RA=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_stars_conjunctions_RA[2]=t.astimezone(HKT).date()
            temp_list_stars_conjunctions_RA[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
            # temp_list_stars_conjunctions_RA[3]=t.utc_datetime()
            temp_list_stars_conjunctions_RA[4]=''
            temp_list_stars_conjunctions_RA[1]=name_list_eng[i]
            temp_list_stars_conjunctions_RA[0]=name_list_chi[i]
            temp_list_stars_conjunctions_RA[5]='?'
            phase = almanac.moon_phase(eph, t)
            # if i ==0 or i == 5 or i == 6:
            #     temp_list_stars_conjunctions[8]='3' 
            # if i == 2 or i ==3 or i ==4: # Mars, jupiter and saturn
            if phase.degrees > 330 or phase.degrees <30:
                temp_list_stars_conjunctions_RA[5]=3
            elif phase.degrees > 300 or phase.degrees <60:
                temp_list_stars_conjunctions_RA[5]=2
            else:
                temp_list_stars_conjunctions_RA[5]=1
            print(temp_list_stars_conjunctions_RA)
            phase = almanac.moon_phase(eph, t)
            # print('Moon phase: {:.1f} degrees'.format(phase.degrees))
            # if phase.degrees >25, =1; d=317.6, =2; dd=296, =1
            list_stars_conjunctions_RA.append(temp_list_stars_conjunctions_RA)      
