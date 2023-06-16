# Astronomical Events List Generator
To generate a list of astronomical events within a specified time range (e.g.: 1/1/2023 - 31/12/2023) and save it into an Excel file. This Excel file is formatted according to the Astro e-calender of the Hong Kong Space Museum.

New updates:
1. A .CSV file for google calendar will also be saved. Before importing into google calendar, users have to open the file using Excel and check the following:
    - Change the format of "Start Time and "End Time" so that it appears as HH:MM:SS in Excel.
    - Change the format of "Start Date" and "End Date" of all meteor shower events so that it appears as DD/MM/YYYY in Excel.
    - Update the description of meteor shower events, including the latest ZHR from IMO website.
2. Added new files:
    - twilight.py: provide the time when the astronomical twilight starts and ends.
    - all_year_sunrise_sunset.py: provide the time of sunrise and sunset.
    - planet_moon_rise_set.py: provide the rise time and set time of all planets and the Moon.
    - Rise, set and twilight.xlsx: Generated result of the above time information in 2023. Saved in the output folder.
3. Solar eclipse is included, but please see the explanation below.
4. Lunar appulse is limited to specific conditions, please see the explanation below. 
    
## How to run

Download all the above files from the button “Code” -> “Download ZIP”. Unzip the folder and place all .py files under the same folder.

Python programming language has to be installed on the computer. For simplicity, the user may install the Anaconda Distribution which includes the latest Python versions and many useful Python modules including jupyter, Numpy, pandas, Spyder, etc. To install Anaconda, please go to
https://www.anaconda.com

After installing Anaconda, open the Spyder software and load the file “main.py”. You should see something like this:

```python
from skyfield import api, almanac
import pandas as pd
from skyfield.api import wgs84, N, S, E, W
from pytz import timezone

ts = api.load.timescale()
eph = api.load('de440.bsp')
...
```
While the program runs, the main.py will call other .py files in the same folder. Check the "Output selection" paragraph below before you run main.py. For trial purpose, you can set a shorter time period such as:

```python
t0 = ts.utc(year, 1, 1) - 1/3
t1 = ts.utc(year, 1, 3) - 1/3
```

Then, only data for 2 days will be generated. If it is the first time to run the program, internet connection is required for it to download the ephemeris (e.g.:DE440.bsp). If `ModuleNotFoundError` appears, install the Python modules by typing/copying the following commands in Spyder’s console and press Enter.

```python
pip install skyfield
```
```python
pip install pytz
```
```python
pip install pandas
```
```python
pip install bs4
```

Whenever the `ModuleNotFoundError` appears, you can install the module by typing “pip install [module name]”, then the program should be able to proceed.

If Python is installed in another way where the Anaconda Distribution is not used, the above modules have to be installed from the terminal or command prompt (cmd). However, if the modules are installed into a different root/directory/environment other than the Python program itself, these modules cannot be located when the program is executed. The safest way is to execute the program first and let the computer tell you which module is absent, then install the module from the same command window.

If everything is correct, you should be able to see the astronomical data from the command window, and an Astro E-calendar [year] raw.xlsx will be saved under the same folder with the .py files. Adjust the time range to generate all the data you want, such as:

```python
t0 = ts.utc(year, 1, 1) - 1/3
t1 = ts.utc(year, 12, 31) - 1/3
```


## Ephemerides 

Ephemerides data are computed based on an ephemeris. Here the NASA JPL Planetary and Lunar Ephemerides DE440 is used. For more information about DEXXX, please visit:
https://ssd.jpl.nasa.gov/planets/eph_export.html

The ephemeris file will be downloaded when the program runs. To compute the data based on another ephemeris, for example, to simulate MICA(version 2.2.2)'s result, DE405 has to be used by modifying the ephemeris name as:
```python
eph = api.load('de405.bsp')
```
Then the program will download DE405 and compute the data based on that ephemeris. However, there should be no difference between DE405 and DE440 when dealing with such basic astronomical events.

## Meteor shower data

The meteor shower data (Quadrantids, Perseids, Geminids, Lyrids, Orionids, Leonids) are obtained by reading the HTML data from IMO website: https://www.imo.net/members/imo_showers/working_shower_list

Users have to update the format of the dates (e.g.: 13Aug2022 -> 2022-08-13) manually and input the predicted peak time from the IMO’s Meteor Shower Calendar (pdf document from IMO’s resources page).

If the format of this IMO website is changed, the program will generate incorrect information.

Since the IMO website above provides the meteor shower of the current year only, the program will always give the same result even if another year is selected.

## Compare with MICA
This program uses a Python module - Skyfield where most of its generated data fit perfectly with MICA's output. However, there are some modifications as explained below:

**Rounding of number**

It was found that MICA rounds off incorrectly sometimes. Please observe the following events:

```
Sunset 2021-7-3 19:11:30; MICA 19:11; NAOJ: 19:12 (may be due to Delta T)
Full moon 2021-12-19 12:35:30; MICA 12:35; NAOJ 12:36, China 12:36 (may be due to Delta T)
Full moon 2023-4-6 12:34:31; MICA 12:34
Full moon 2023-4-20 12:12:32; MICA 12:12
Full moon 2023-9-29 17:57:32; MICA 12:57
Neptune Moon Conjunction 2023-11-22 15:45:31; MICA 15:45
```

Other sources such as the Purple Mountain Observatory, China, and the National Astronomical Observatory of Japan round the time off to the nearest minute. The reason why MICA does not round them off is unknown. This program will round the time off to the nearest minute or mostly second, if available.

**Conjunction and Appulse**

A conjunction is not defined as the closest angular separation between two objects. However, in some situations, it is worth listing the moment of appulse, especially when an occultation happens. For example, a lunar occultation of Uranus looks like this: 

```
Occultation starts (disappearance): 18:58
Occultation ends (reappearance): 19:47
Uranus Moon Conjunction (right ascension): 21:11
```

The conjunction happens after the reappearance of Uranus, meaning that Uranus has already left the moon disc completely. Here, we add the prediction of appulse: 

```
Occultation starts (disappearance): 18:58
Uranus Moon Appulse: 19:22
Occultation ends (reappearance): 19:47
```
The sequence looks more intuitive, but MICA does not offer appulse. This program offers predictions on conjunction and appulse, but please see the explanation session below about the condition of appulse.

## Output selection

The main.py will import and execute other .py files and generate a .xlsx file. The user may reduce the number of events to be executed by making a code line as a comment. Such as:
```python
if __name__ == '__main__':
    from season_events import *    
    from moon_phase import *    
    ...
    list0.extend(
        list_SEASON_EVENTS +
        list_moon_phases +
        ...
        )
 ```
Only the data of seasonal points and moon phases will be generated.
```python
if __name__ == '__main__':
    from season_events import *    
#   from moon_phase import *    
#    ...
    list0.extend(
        list_SEASON_EVENTS
#       list_moon_phases +
#        ...
        )
 ```
Only the data of seasonal points will be generated. Remember to delete the "+" if the comment line is the last line.

To generate a list of events of another year, simply change the variable  ```year``` .

```python
HKT = timezone('Asia/Hong_Kong')
year = 2023
t0 = ts.utc(year, 1, 1) - 1/3
t1 = ts.utc(year, 12, 31) - 1/3
 ```
 Here the events from 1/1/2023 to 31/12/2023 will be generated. the ```-1/3``` accounts for the timezone UTC+8.
  
The output file is named as Astro E-calendar [year] raw.xlsx. It is recommended to remove "raw" when the solar eclipse information and meteor shower information are updated. In the output folder, you can find a completed "Astro E-calendar 2023.xlsx" and some raw files for the future.
 
## Level

This program distinguishes each astronomical event into different levels. Some events are defined as level 1 such as moon phases, while some other events like Moon at perigee, superior conjunction, etc, are level 3. Considerations are made for complicated events such as planetary appulse, for example:

```python
if int(earth.at(t).observe(planet_list_top[i]).phase_angle(sun).degrees) >150:
    temp_list_planetary_appulse[5]=3
elif int(earth.at(t).observe(planet_list_top[i]).phase_angle(sun).degrees) > 120:
    if planetary_appulse_degrees < 1:
        temp_list_planetary_appulse[5]=1
    else:
        temp_list_planetary_appulse[5]=2
else:
    temp_list_planetary_appulse[5]=1
if j == 5 or j == 6:
    temp_list_planetary_appulse[5]=3
```
If the first planet has a phase angle above 150 degrees, that means the angular separation between the Sun and the first planet is within 30 degrees, then the event will always be marked as level 3 since it is hardly observable.

If the angular separation between the Sun and the first planet is between 30 degrees and 60 degrees, and the separation between the two planets is smaller than 1 degree, then the event will be marked as level 1. Otherwise, the events will be marked as level 2.

In the remaining case where the angular separation between the Sun and the first planet is larger than 60 degrees, the events will always be marked as level 1.

For Uranus and Neptune (i.e.: j=5 and 6, defined in a Python list), the events will always be marked as level 3.

## Remarks, Limitations and Possible Future Updates


- Meteor shower data is obtained by reading HTML data from the IMO website. It provides information on the current year only. To get IMO's prediction, please check IMO's Meteor Shower Calendar.

- The coordinates of stars (RA, DEC) are referred to their position in 2022. For higher precision appulse between stars, occultation, etc, please update the coordinates manually to obtain J(now), it can be found online or from Stellarium. By specifying their proper motion, the latest coordinates can be computed in future updates.

- An occultation event will be marked if the appulse between the stars or planets and the moon is less than 0.25 degrees. This number can be refined.

- The earliest or latest sunrise and sunset time are not the same for different latitudes.
```python
if  ti.astimezone(HKT).month == 1:
```
To find the latest sunset, only January is considered in this program as the latest sunset in Hong Kong is always within January.
```python
if  ti.astimezone(HKT).month== 6 or ti.astimezone(HKT).month== 7:
 ```
As an example, if an event may occur in June or July, the program should be written as above.

- Excel reads time as 0 to 1. So you can see a decimal number in the time column. You can adjust its format in Excel.

- For enquiry, please contact Mr. CHAN Chun-lam (chlchan@lcsd.gov.hk).

## Explanation

**solar_eclipse.py**

Find the moment when the moon touches the limb of the Sun. Solar eclipse prediction depends on how you "select" the radius of the Sun and the Moon. Here, the nominal solar radius, Rs=695700, is adopted. The radius of the Moon is explained in the "lunar_eclipse.py" below. However, the prediction does not include total solar eclipse and annular solar eclipse as second contact and third contact between the Sun and the Moon are not included yet.

**lunar_eclipse.py**

Find the moment when the moon touches the edge of the Earth's umbra and penumbra. Lunar eclipse prediction depends on how you "select" the radius of the moon. Here, the IAU adopted value k = 0.2725076 is used as default, where Moon's radius = Earth's radius x k. Users may change the parameter to achieve better prediction.

**lunar_appulse.py, stars_lunar_appulse.py**

Show the moment of smallest angular separation between the Moon and the planets or stars under the following conditions:

1. Separation is less than 1 degree;
2. The Moon is above the horizon;
3. The Sun is at least 15 degrees below the horizon.
 
 When the separation is less than the apparent radius of the Moon. A remark "Occultation" will be shown. For examples (Hong Kong):
 
'天王星、月球最小角距(掩)', 'Uranus-Moon Appulse(Occultation)', datetime.date(2022, 11, 8)... 
  
 '金星、月球最小角距(掩)', 'Venus-Moon Appulse(Occultation)', datetime.date(2023, 3, 24)... 

 '火星、月球最小角距', 'Mars-Moon Appulse', datetime.date(2025, 6, 1)... 
 
 '木星、月球最小角距(掩)', 'Jupiter-Moon Appulse(Occultation)', datetime.date(2034, 10, 25)... 
 
 '土星、月球最小角距(掩)', 'Saturn-Moon Appulse(Occultation)', datetime.date(2037, 2, 2)...

**planetary_appulse.py**

Show the smallest angular separation between two planets, only separation predictions less than 5 degrees are considered as large-angle planetary appulse between the inner planets and outer planets occur oftenly. Obviously, the predicted data are close to those in "planetary_conjunctions_RA.py".
 
**moon_apogee_perigee.py**

Find the exact moment when the Moon is farthest (apogee) or nearest(perigee) from the Earth, without considering the traveling time of light between the Moon and the Earth. In other words, it is not the apparent moment when the Moon is at the farthest or nearest. This program calculates the geometric position of the Moon, not the astrometric, but users are able to change it in this file.
