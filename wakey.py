import keyboard, time, sys
import os, logging
import ctypes
from datetime import datetime 

def main(duration, frequency, verbose, log):

    starttime = time.perf_counter()

    if log:
        # Setup logging
        file, ext = os.path.splitext(__file__)
        logfile = file+'.log'
        logging.basicConfig(filename=logfile, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%b-%d-%y %H:%M:%S')

    if sys.platform == "win32":
        #cmd = 'mode 30,10'
        #os.system(cmd)
        ctypes.windll.kernel32.SetConsoleTitleW('Wakey')
        keypress = 'f15'

    if sys.platform == 'linux':
        if os.getuid() != 0:
            print("Wakey needs to run as root/sudo. Please try relaunch")
            sys.exit()
        else:
            keypress = 'shift'


    # time.sleep() is in seconds. Multiple minutes wanted by 60 seconds to get delay
    delay = frequency * 60 
    thumb = "\U0001F44D"
    computer = "\U0001F5A5\U0000FE0F"
    print(f"Keeping {computer}  awake {thumb}")
    if verbose:
        print(f'Pressing {keypress} every {delay} seconds')

    while True:
        try:
            if sys.platform == "win32":
                keyboard.press_and_release(keypress)
                if verbose:
                    print(f'Button {keypress} was pressed at {currenttime()}')
                    
                if log:
                    logging.info(f'Button {keypress} was pressed at {currenttime()}')
            
            if sys.platform == "linux":
                keyboard.press_and_release(keypress)

            time.sleep(delay)  # Sleep for the amount of seconds generated
            if duration: 
                scriptduration = time.perf_counter() - starttime
                if scriptduration > duration:
                    print("Time duration reached. Ending Wakey.")
                    sys.exit()
        except KeyboardInterrupt:
            # quit
            sys.exit()
            
            
def currenttime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
    
    

# If we are running the file directly, lets add some arguments for our script. 
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simply keep your computer awake and session active")
    parser.add_argument("-d", "--duration", type=int, help="Length of time in minutes, default is forever")
    parser.add_argument("-f", "--frequency", type=int, help="Frequency of keypress in minutes, default is 1 minute", default=1)
    parser.add_argument("-v", "--verbose", action='store_true', help="Verbosely see the output in the console")
    parser.add_argument("-l", "--log", action='store_true', help="Creates a log of the application for later reference")

    # gather arguments
    args = parser.parse_args()
    duration = args.duration
    frequency = args.frequency
    verbose = args.verbose
    log = args.log

    main(duration, frequency, verbose, log)