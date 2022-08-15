from skyfield import api
from skyfield import almanac
from pytz import timezone
from main import t0, t1, eph, HKT

target=['MERCURY BARYCENTER', 
        'VENUS BARYCENTER', 
        'MARS BARYCENTER', 
        'JUPITER BARYCENTER', 
        'SATURN BARYCENTER', 
        'URANUS BARYCENTER', 
        'NEPTUNE BARYCENTER', 
        'PLUTO BARYCENTER', 
        'SUN', 
        'MERCURY', 
        'VENUS', 
        ]
Opposition_eng=['Superior Conjunction of Mercury', 
        'Superior Conjunctionof Venus', 
        'Opposition of Mars', 
        'Opposition of Jupiter', 
        'Opposition of Saturn', 
        'Opposition of Uranus', 
        'Opposition of Neptune', 
        'Opposition of Pluto', 
        ]
Opposition_chi=['水星上合', 
        '金星上合', 
        '火星衝', 
        '木星衝', 
        '土星衝', 
        '天王星衝', 
        '海王星衝', 
        '冥王星衝', 
        ]
Conjunction_eng=['Inferior Conjunction of Mercury', 
        'Inferior Conjunction of Venus', 
        'Conjunction of Mars', 
        'Conjunction of Jupiter', 
        'Conjunction of Saturn', 
        'Conjunction of Uranus', 
        'Conjunction of Neptune', 
        'Conjunction of Pluto', 
        ]
Conjunction_chi=['水星下合', 
        '金星下合', 
        '火星上合', 
        '木星上合', 
        '土星上合', 
        '天王星上合', 
        '海王星上合', 
        '冥王星上合', 
        ]
list_oppositions_conjunctions=[]
for i in range(8):
    f = almanac.oppositions_conjunctions(eph, eph[target[i]])
    t, y = almanac.find_discrete(t0, t1, f)

    for yi, ti in zip(y, t):
        temp_list_oppositions_conjunctions=['0=year', '1=month','2=date','3=hour','4=minute','5=second','6=event_Eng','7=event_Chi']
        temp_list_oppositions_conjunctions[0]=ti.astimezone(HKT).year
        temp_list_oppositions_conjunctions[1]=ti.astimezone(HKT).month
        temp_list_oppositions_conjunctions[2]=ti.astimezone(HKT).day
        temp_list_oppositions_conjunctions[3]=ti.astimezone(HKT).hour
        temp_list_oppositions_conjunctions[4]=ti.astimezone(HKT).minute
        temp_list_oppositions_conjunctions[5]=int(ti.astimezone(HKT).second)
        if yi==0:
            temp_list_oppositions_conjunctions[6]=Conjunction_eng[i]
            temp_list_oppositions_conjunctions[7]=Conjunction_chi[i]
        if yi==1:
            temp_list_oppositions_conjunctions[6]=Opposition_eng[i]
            temp_list_oppositions_conjunctions[7]=Opposition_chi[i]
        
        list_oppositions_conjunctions.append(temp_list_oppositions_conjunctions)
        print(temp_list_oppositions_conjunctions)  