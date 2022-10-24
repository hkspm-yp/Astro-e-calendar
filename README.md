# Astronomical Event list generator
To generate a list of astronomical events within a specified time range (e.g.: 1/1/2023 - 31/12/2023) and save it into an excel file. This excel file is made according to the Astro e-calander of the Hong Kong Space Museum.

## How to run

Download all the above files from the button “Code” -> Download ZIP. Unzip the folder and put all .py files under the same folder.

Python programming language has to be installed to the computer. For simplify, user may install the Anaconda Distribution which includes the latest python versions and many useful python packages including jupyter, Numpy, pandas and Spyder, etc. To install Anaconda, please go to
https://www.anaconda.com

After installing Anaconda, open the Spyder software and load the file “main.py”. You should see something like:
After installing Anaconda, open the Spyder software and load the file “main.py”. You should see something like:

```python
from skyfield import api
from skyfield import almanac
import pandas as pd
from pytz import timezone
ts = api.load.timescale()
eph = api.load('de440.bsp')
...
```

You can try to run “main.py” in Spyder. If “package not found” error appears, install the python packages by typing the following commands in Spyder’s terminal.

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

Whenever the “package not found” error appears, you can install the package by typing “ pip install [package name]”, then the programme should be able to proceed.

If the Python programming language is installed in another way where the Anaconda Distribution is not used. The above packages have to be installed from the terminal or command prompt (cmd). However, if the packages are installed into a different root/directory/environment other than the python programme itself, these packages cannot be located when the programme is executed. The safest way is to execute the programme first and let the computer tells you which package is not found, then install the package from the same command window.

If everything is correct, you can see the astronomical data from the command window, and an output[year].xlsx will be saved under the same folder of the .py files.


## Useful tips

Ephemeris data are computed based on an ephemeris. Here the NASA JPL Planetary and Lunar Ephemerides DE440 is used. For more information about DEXXX, please go to:
https://ssd.jpl.nasa.gov/planets/eph_export.html

The ephemeris file will be downloaded when the programme runs, to compute the data based on another ephemeris. For example, the MICA software (version 2.2.2) uses DE405. To simulate MICA's result, DE405 has to be used by modifying the ephemeris name as:
```python
eph = api.load('de405.bsp')
```
Then the programme will download DE405 and compute the data based on that ephemeris.

## Meteor shower data

The meteor shower data (Quadrantids, Perseids, Geminids, Lyrids, Orionids, Leonids) are obtained by reading the HTML data from the IMO website: https://www.imo.net/members/imo_showers/working_shower_list

User has to update the format of the dates (e.g.: 13Aug2022 -> 2022-08-13) manually and input the predicted peak time from the IMO’s Meteor Shower Calendar (pdf document form IMO’s resources page).

If the format of this IMO website is changed, the programme will generate incorrect information.


## Discrepancy in MICA
This programme use a python package - Skyfield where most of its generated data fit perfectly with MICA's output. However, there some changes applied as explained below:

**Rounding of number**

It was found that MICA does the rounding incorrectly sometime. Please observe the following events:

```
Full moon 2023-4-6 12:34:31; MICA reports 12:34
Full moon 2023-4-20 12:12:32; MICA reports 12:12
Full moon 2023-9-29 17:57:32; MICA reports 12:57
Neptune Moon Conjunction 2023-11-22 15:45:31; MICA reports 15:45
```

Other sources such as the Purple Mountain Observatory, China and National Astronomical Observatory of Japan round the time up to the nearest minute. Reason why MICA does not round them up is unclear.

**Defination of conjuction**

MICA defines planetary conjuction happens when the objects(planet+moon/planet+planet) share the same right ascension. However, many other sources defines planetary conjuction when the two planets share the same ecliptic longitude. In skyfield, both defination can be used depends on how the programme is written. But please see below.

**Conjunction vs Appulse**

Conjunction is not defined as the closet angular separation before two objects. However, the public concerns the closest moment only. Hence, in this programme, the closest angular separation, or appulse, is reported rather than conjunction. Please observe this case where on 2022-11-08, a total lunar eclipse and a Lunar occultation of Uranus happens at the same time. 

```
Occultation starts (disappearance): 18:58
Occultation ends (reappearance): 19:47
Uranus Moon Conjunction (right ascension): 21:11
```

In conjunction, the event happens after the reappearance of Uranus, which means Uranus has already left the moon disc completely. It is obvious that Uranus has already passed the closet separation to the moon. However, if appulse is used to replace conjunction, then we have:

```
Occultation starts (disappearance): 18:58
Uranus Moon Appulse: 19:22
Occultation ends (reappearance): 19:47
```
The sequence looks more intuitive, but MICA does not offer appulse.

## Output selection

The main.py will import and execute other .py file and generate an .xlsx file. User may reduce the events to be executed by making a code line as a comment. Such as:
```python
if __name__ == '__main__':
    from season_events import *    
    from moon_phase import *    
    list0.extend(
        list_SEASON_EVENTS +
        list_moon_phases
        )
 ```
Only the data of seasonal points and moon phases will be generated.
```python
if __name__ == '__main__':
    from season_events import *    
#    from moon_phase import *    
    list0.extend(
        list_SEASON_EVENTS
#        list_moon_phases
        )
 ```
Only  the data of seasonal points will be generated. Do remember  to delete the "+" before the comment line
