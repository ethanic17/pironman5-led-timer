# pironman5-led-timer

A simple python script that functions as a system daemon to turn off the fan & LEDs on the Pironman5 case at night (or to any desired time). Only works on Pironman5 Case. 

Installation:
- Make sure the Pironman5 package is installed and the service daemon is running 
- Clone the repository to your Pi
- Place the service file inside of the ```/etc/systemd/system``` directory.
- Run the command ```python3 -m venv /home/pi/venv``` to create a python virtual enviornment
- Then, reload the daemon and start the service
  - ```sudo systemctl daemon-reload```
  - ```sudo systemctl enable led_timer.service```
  - ```sudo systemctl start led_timer.service```


FYI:
- You can change the time to something else in the python file, just use a 24 hour format (right now it is set to turn on at 9AM and turn off at 9PM)
- If your username isn't `pi`, open the service file and change `pi` to your username
- If the script (```config.py```) is placed in a different directory, make sure to change that in the service file as well
- Make sure python is installed (should be pre-installed on Raspberry Pi OS)

<img src="https://github.com/user-attachments/assets/f31175e6-8920-448b-9aea-66921ae69571" width="500">


