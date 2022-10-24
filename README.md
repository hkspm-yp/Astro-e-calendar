# Astronomical Event list generator
To generate a list of astronomical events within a specified time range and save it into an excel file. This excel file can be used as the Astro e-calander of the Hong Kong Space Museum


To generate a list of astronomical events within a specified time range (e.g.: 1/1/2023 - 31/12/2023) and save it into an excel file. This excel file is made according to the Astro e-calander of the Hong Kong Space Museum.

## How to run

Download all the above files from the button “Code” -> Download ZIP. Unzip the folder and put all .py files under the same folder.

Python programming language has to be installed to the computer. For simplify, user may install the Anaconda Distribution which includes the latest python versions and many useful python packages including jupyter, Numpy, pandas and Spyder, etc. To install Anaconda, please go to
https://www.anaconda.com

After installing Anaconda, open the Spyder software and load the file “main.py”. You should see something like:
After installing Anaconda, open the Spyder software and load the file “main.py”. You should see something like:

```python
ts = api.load.timescale()
eph = api.load('de440.bsp')
HKT = timezone('Asia/Hong_Kong')
t0 = ts.utc(2021, 1, 1) - 1/3
t1 = ts.utc(2021, 12, 31) - 1/3
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

The ephemeris file will be downloaded when the programme starts, to compute the data based on another file. For example, the MICA software (version 2.2.2) uses DE405, to simulate MICA result, DE405 has to be used by modifying the ephemeris name as:
```python
eph = api.load('de405.bsp')
```
Then the programme will download DE405 and compute the data based on that ephemeris.

