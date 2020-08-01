# Pomodoro Timer

Pomdoro Timer is a desktop application that allows you to apply the pomodoro technique to managing your time on any task. 

The technique breaks down work into timed intervals called 'pomodoros', typically of 25 minutes, followed by a 5 minute break. After 2 pomodoros, there is a longer break of 10 minutes, and the cycle repeats.

The app is configured to the above time lengths by default, but they are customisable within the app.

![timer-ui](https://github.com/mc-anon/tk-pomodoro-timer/blob/assets/pomodoro-screenshot-timer.png 
)

Pomodoro Timer is based on a project from this course for Tkinter on Udemy: https://www.udemy.com/course/desktop-gui-python-tkinter/

The aim is to extend the functionality of the original.


## Notes before use

Open up a Terminal and check your local Python version:
```shell script
$ python3 -V
``` 
The app requires at least Python3.6 to run. I have been using version 3.8.2 locally.
If you don't have a suitable version, you can install it from here: https://www.python.org/downloads/

If you're a regular Python user, you may be using pyenv to handle your Python versions. 
There seems to be issues with pyenv installed versions of Python and the tkinter GUI module that the app uses.
I was unable to get the app working even after following solutions offered in this thread:

https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos

Please let me know if you're able to find a solution or workaround.
In the meantime, please use your system's Python to run the app.

# Setup
## With virtual environment
With Python development it's best to create a virtual environment for each project. 
This way you can bind an application to a particular version of the included packages/modules.

Assuming you have a suitable version of Python3 installed: 
- Open a Terminal window in the project folder.
- Create the virtual environment (best to keep this elsewhere):
```shell script
$ python3 -m venv /path/to/new/virtual/environment
``` 
- Activate it
        
On Windows, run:
```shell script
> your-env\Scripts\activate.bat
```

On Unix or MacOS, run:
```shell script
$ source your-env/bin/activate
```

- Install packages:
```shell script
$ pip3 install -r requirements.txt
```

## Without virtual environment
If you don't wish to create a virtual environment, and assuming you have a suitable version of Python3 installed:

- Open a Terminal window inside the project folder.
- Install packages:
```shell script
$ pip3 install -r requirements.txt
```

NB: With this method, if any of the included packages are updated at a later stage, the app may not run.


# Usage
Simply open a Terminal window in the project folder and run:

```shell script
$ python3 app.py
``` 

Make sure you activate the appropriate virtual environment first.
If you want to deactivate the environment at any point, simply run:
```shell script
$ deactivate
```

# Contributing
1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

# Notes
30/07/2020
- Tried to use PyInstaller to build an executable file for macOS, but PyInstaller is not yet compatible with Python 3.8.
- Tried using pyenv to install an earlier version of Python (3.7) and try PyInstaller again, turns out there are issues with pyenv installed Python versions and tkinter (GUI module).
- Tried using another machine with Python 3.7 as the system version. PyInstaller was able to build the package, but the app fails at runtime as it is unable to find some data files for some reason. 
- Tried Docker, couldn't get tcl/tk to work in the container

If you can help me distribute this as an executable file, let me know!
