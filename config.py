import time 
from datetime import datetime 
import subprocess

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "21:00": # 9:00 PM
        subprocess.call(["pironman5 -gm 4"], shell=True)
        subprocess.call(["pironman5 -re false"], shell=True)
        subprocess.call(["sudo systemctl restart pironman5.service"], shell=True)
        time.sleep(60)
    if current_time == "09:00": # 9:00 AM
        subprocess.call(["pironman5 -gm 0"], shell=True)
        subprocess.call(["pironman5 -re true"], shell=True)
        subprocess.call(["sudo systemctl restart pironman5.service"], shell=True)
        time.sleep(60)
    time.sleep(60)

   
    


