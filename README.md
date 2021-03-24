# Wakey

Keeps the computer awake by simulating a F15 keyboard press and release.

Default key press is currently 1 minute. There are arguments to change the frequency as well.

Currently tested on Windows 10 and Ubuntu 20.10 (Groovy Gorilla), but no reason it should not work on other operating systems that have Python 3.6+ installed.

## Setup

To setup and start using Wakey, just download the [Latest Release](https://github.com/cjerrington/wakey/releases/latest) and then install the dependencies.

```shell
git clone https://github.com/cjerrington/wakey.git
cd wakey
pip install -r requirements.txt
```

You can install this in a virtual environment as well, which is what I'd prefer. To get started run...

```shell
pip install virtualenv
virtualenv .
scripts\activate
pip install -r requirements.txt
python wakey.py
```

## Arguments

Wakey has a few arguments you can use to adjust the settings.

Command | Explanation
--------|------------
-d, --duration | Used to set the duration to run Wakey
-f, --frequency | Used for the frequency of the keypress in minutes. Default is 1 minute.
-v, --verbose | To see the output of the keypress in the console. Default is false.
-l, --log | Create a log of the application to see when the events happened. Default is false

## Usage

Wakey will run with no arguments given and use the default settings. On windows this is the F15 key and every 1 minute. On Linux we need to run `wakey.py` as a root user. To avoid depending on X, the Linux parts reads raw device files (/dev/input/input*) but this requires root. Part of the [known limitations](https://pypi.org/project/keyboard/) for the keyboard module.

On Linux Wakey uses the shift key and on Windows Wakey uses the function 15 key (F15).

### Example

This will run Wakey with a keypress every 2 minutes showing the output to the screen and create log file

```shell
python wakey.py -f 2 -v -l
```

The log file will be created in the same directory as Wakey.

```shell
python wakey.py -d 5
```

Duration is in minutes.

## Building

You can compile Wakey to an executable (tested on Windows 10).
There is the built in ```build.bat``` file which uses ```pyinstaller```

```shell
pyinstaller --onefile --icon=sun.ico --version-file=version.txt wakey.py
```

This step has already been done for you and you can find the latest compiled version [here](https://github.com/cjerrington/wakey/releases/latest). Currently only supporting Windows for the pre-compiled versions.

## Todo

Things I'd like to add to Wakey

- [X] Add support for logging
- [X] Add support for changing the frequency
- [X] Add support Linux
- [ ] Mouse support instead of keyboard
- [X] Add duration for the script to run, example for 5 minutes, and hour. Currently Wakey runs until the program quits.

## Images

![help](imgs/help.png)

![verbose](imgs/verbose.png)
