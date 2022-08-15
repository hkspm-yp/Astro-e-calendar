from skyfield.framelib import ecliptic_frame
from skyfield.searchlib import find_minima
from main import *
from pytz import timezone

planet_list=[mercury, venus, mars, jupiter, saturn, uranus, neptune]
name_list_chi=['水星合月', '金星合月', '火星合月', '木星合月', '土星合月', '天王星合月','海王星合月']
name_list_eng=['Mercury Moon Conjunction',
               'Venus Moon Conjunction',
               'Mars Moon Conjunction',
               'Jupiter Moon Conjunction',
               'Saturn Moon Conjunction',
               'Uranus Moon Conjunction',
               'Neptune Moon Conjunction']
list_lunar_conjunctions=[]
for i in range(7):
    def separation_at(t):
        e = earth.at(t)
        s = e.observe(moon).apparent()
        m = e.observe(planet_list[i]).apparent()
        return s.separation_from(m).degrees

    separation_at.step_days = 15.0

    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        temp_list_lunar_conjunctions=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
        temp_list_lunar_conjunctions[0]=t.astimezone(HKT).year
        temp_list_lunar_conjunctions[1]=t.astimezone(HKT).month
        temp_list_lunar_conjunctions[2]=t.astimezone(HKT).day
        temp_list_lunar_conjunctions[3]=t.astimezone(HKT).hour
        temp_list_lunar_conjunctions[4]=t.astimezone(HKT).minute
        temp_list_lunar_conjunctions[5]=int(t.astimezone(HKT).second)
        temp_list_lunar_conjunctions[6]=name_list_eng[i] + ' (' + str("%0.2f" % separation_degrees) +'°)'
        temp_list_lunar_conjunctions[7]=name_list_chi[i] + ' (' + str( "%0.2f" % separation_degrees) +'°)'
        print(temp_list_lunar_conjunctions)
        list_lunar_conjunctions.append(temp_list_lunar_conjunctions)      