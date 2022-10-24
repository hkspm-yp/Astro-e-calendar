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

You can try to run “main.py” in Spyder. If the “package not found” error appears, install the python package by typing the following commands in Spyder’s terminal.

```python
Pip stall skyfield
```
```python
Pip stall pytz
```
```python
Pip stall pandas
```
```python
Pip stall bs4
```

Several python packages are also required. These packages can be installed by typing the following commands in the terminal or command prompt (cmd). However, if the packages are installed into a different root/directory/environment other than the python programme itself, these package cannot be located when the programme is executed and For beginner, when the Anaconda Distribution is installed, 
