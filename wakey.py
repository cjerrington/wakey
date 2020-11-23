import keyboard, time, sys
import ctypes
import os

if sys.platform == "win32":
    cmd = 'mode 30,10'
    os.system(cmd)
    ctypes.windll.kernel32.SetConsoleTitleW('Wakey')


print("Keeping computer awake :)")

while True:
    try:
        keyboard.press_and_release('f15')
        delay = 300 # 5 minutes
        time.sleep(delay)  # Sleep for the amount of seconds generated
    except KeyboardInterrupt:
        # quit
        sys.exit()