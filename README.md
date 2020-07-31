# tk-pomodoro-timer

30/07/2020
- Tried to use PyInstaller to build an executable file for macOS, but PyInstaller is not yet compatible with Python 3.8.
- Tried using pyenv to install an earlier version of Python (3.7) and try PyInstaller again, turns out there are issues with pyenv installed Python versions and tkinter (GUI module).
- Tried using another machine with Python 3.7 as the system version. PyInstaller was able to build the package, but the app fails at runtime as it is unable to find some data files for some reason. 
- Tried Docker, couldn't get tcl/tk to work in the container
