from skyfield import api
from skyfield import almanac
from pytz import timezone
from main import *

target=['MERCURY BARYCENTER', 
        'VENUS BARYCENTER', 
        'MARS BARYCENTER', 
        'JUPITER BARYCENTER', 
        'SATURN BARYCENTER', 
        'URANUS BARYCENTER', 
        'NEPTUNE BARYCENTER', 
        # 'PLUTO BARYCENTER', 
        ]
Opposition_eng=['Superior Conjunction of Mercury', 
        'Superior Conjunction of Venus', 
        'Opposition of Mars', 
        'Opposition of Jupiter', 
        'Opposition of Saturn', 
        'Opposition of Uranus', 
        'Opposition of Neptune', 
        # 'Opposition of Pluto', 
        ]
Opposition_chi=['水星上合', 
        '金星上合', 
        '火星衝', 
        '木星衝', 
        '土星衝', 
        '天王星衝', 
        '海王星衝', 
        # '冥王星衝', 
        ]
Conjunction_eng=['Inferior Conjunction of Mercury', 
        'Inferior Conjunction of Venus', 
        'Conjunction of Mars', 
        'Conjunction of Jupiter', 
        'Conjunction of Saturn', 
        'Conjunction of Uranus', 
        'Conjunction of Neptune', 
        # 'Conjunction of Pluto', 
        ]
Conjunction_chi=['水星下合', 
        '金星下合', 
        '火星上合', 
        '木星上合', 
        '土星上合', 
        '天王星上合', 
        '海王星上合', 
        # '冥王星上合', 
        ]
list_oppositions_conjunctions=[]
for i in range(7): # range(8) if Pluto is considered.
    f = almanac.oppositions_conjunctions(eph, eph[target[i]])

    t, y = almanac.find_discrete(t0, t1, f)

    for yi, ti in zip(y, t):
        temp_list_oppositions_conjunctions=['0=event_Chi', '1=event_Eng','2=date(dd/mm/yyyy)','3=time(hh/mm)','4=remark','5=level']
        temp_list_oppositions_conjunctions[2]=ti.astimezone(HKT).date()
        temp_list_oppositions_conjunctions[3]=(float(ti.astimezone(HKT).time().hour)+float(ti.astimezone(HKT).time().minute)/60+float(ti.astimezone(HKT).time().second)/3600)/24
        # temp_list_oppositions_conjunctions[3]=t.utc_datetime()
        temp_list_oppositions_conjunctions[4]=''       
        temp_list_oppositions_conjunctions[5]='?'
        if i == 0 or i ==1 or i == 6 or i ==7:
            temp_list_oppositions_conjunctions[5]=3
        if yi==0:
            temp_list_oppositions_conjunctions[1]=Conjunction_eng[i]
            temp_list_oppositions_conjunctions[0]=Conjunction_chi[i]
            if i == 2 or i ==3 or i ==4 or i ==5:
                temp_list_oppositions_conjunctions[5]=3
        if yi==1:
            temp_list_oppositions_conjunctions[1]=Opposition_eng[i]
            temp_list_oppositions_conjunctions[0]=Opposition_chi[i]
            if i == 2 or i ==3 or i ==4:
                temp_list_oppositions_conjunctions[5]=1
            if i == 5:
                temp_list_oppositions_conjunctions[5]=2
        
        list_oppositions_conjunctions.append(temp_list_oppositions_conjunctions)
        print(temp_list_oppositions_conjunctions)  
