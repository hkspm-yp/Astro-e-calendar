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
list_lunar_conjunctions_RA=[]

for i in range(7):
    def separation_at(t):
        e = earth.at(t)
        s = e.observe(moon).apparent()
        m = e.observe(planet_list[i]).apparent()
        sRa, _, _ = s.radec(epoch = 'date')
        mRa, _, _ = m.radec(epoch = 'date')
        return abs(sRa.hours - mRa.hours)

    separation_at.step_days = 15.0

    separation_times, separation = find_minima(t0, t1, separation_at)

    for t, separation_degrees in zip(separation_times, separation):
        if separation_degrees < 0.1:
            temp_list_lunar_conjunctions_RA=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
            temp_list_lunar_conjunctions_RA[2]=t.astimezone(HKT).date()
            temp_list_lunar_conjunctions_RA[3]=(float(t.astimezone(HKT).time().hour)+float(t.astimezone(HKT).time().minute)/60+float(t.astimezone(HKT).time().second)/3600)/24
            temp_list_lunar_conjunctions_RA[4]=''
            temp_list_lunar_conjunctions_RA[1]=name_list_eng[i] + ' (right ascension)'
            temp_list_lunar_conjunctions_RA[0]=name_list_chi[i] + '（赤經）'
            temp_list_lunar_conjunctions_RA[5]='?'
            phase = almanac.moon_phase(eph, t)
            # if i ==0 or i == 5 or i == 6:
            #     temp_list_lunar_conjunctions[8]='3' 
            # if i == 2 or i ==3 or i ==4: # Mars, jupiter and saturn
            if phase.degrees > 330 or phase.degrees <30:
                temp_list_lunar_conjunctions_RA[5]=3
            elif phase.degrees > 300 or phase.degrees <60:
                temp_list_lunar_conjunctions_RA[5]=2
            else:
                temp_list_lunar_conjunctions_RA[5]=1
            print(temp_list_lunar_conjunctions_RA)
            phase = almanac.moon_phase(eph, t)
            print('Moon phase: {:.1f} degrees'.format(phase.degrees))
            # if phase.degrees >25, =1; d=317.6, =2; dd=296, =1
            list_lunar_conjunctions_RA.append(temp_list_lunar_conjunctions_RA)      