import PyATEMMax
# from matplotlib.pyplot import flag
from yeelight import Bulb
import time
import threading
import socket, sys

STR_GREEN_CONSOLE = "\033[92m"
STR_NORMAL_CONSOLE = "\033[0m"
STR_YELLOW_CONSOLE = "\033[93m"
GLOBAL_BRIGHTNESS = 1

switcher = PyATEMMax.ATEMMax()

def tally_task(input_number):
    last_tally_str = str(switcher.tally.bySource.flags[input_number])
    while True:
        tally_str = str(switcher.tally.bySource.flags[input_number])
        # print(tally_str)
        if last_tally_str != tally_str:
            if tally_str == "[PVW]":
                if "-v" in sys.argv: 
                    print(f"{input_number} is on preview")
                bulbs[input_number - 1].turn_on()
                bulbs[input_number - 1].set_rgb(0,255,0)
                bulbs[input_number - 1].set_brightness(GLOBAL_BRIGHTNESS)
            if tally_str == "[PGM]":
                if "-v" in sys.argv:
                    print(f"{input_number} is on program")
                bulbs[input_number - 1].turn_on()
                bulbs[input_number - 1].set_rgb(255,0,0)
                bulbs[input_number - 1].set_brightness(GLOBAL_BRIGHTNESS)
            if tally_str == "[]": 
                if "-v" in sys.argv:
                    print(f"{input_number} is turned off")
                bulbs[input_number - 1].turn_off()
            last_tally_str = tally_str
        time.sleep(0.01)


def safe_input() -> int:
    """Ensures 'safe' input of int through the command line."""
    while True:
        try:
            inp = int(input())
            break
        except:
            print("invalid input")
    return inp

def get_local_ip() -> str:
    """Getting first three bytes of local IP. Netmask of
    255.255.255.0 is hard-coded. Change possible."""

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
        ip_arr = ip.split('.')
        local_ip = "{0}.{1}.{2}.".format(*ip_arr[:3])
    return local_ip


def setup() -> tuple:
    """Initial setup function"""
    
    print("Enter number of bulbs: ", end="")
    n_bulbs = safe_input()

    print("\nEnter last nibble of the first bulb's IP:")
    print(get_local_ip(), end="")
    ip_start = safe_input()

    return n_bulbs, ip_start

def main():
     # connecting to ATEM
    switcher.connect("192.168.2.111") # TODO more elegant you cunt!
    switcher.waitForConnection()
    if ("-v" in sys.argv):
        print(f"{STR_GREEN_CONSOLE} ATEM connected{STR_NORMAL_CONSOLE}")

    if len(sys.argv) >= 3:
        n_bulbs = int(sys.argv[1])
        ip_start = int(sys.argv[2])
        GLOBAL_BRIGHTNESS = int(sys.argv[3])
    else:
        n_bulbs, ip_start = setup()
    
    global bulbs
    global threads
    threads =list()
    bulbs = list()

    for i in range(n_bulbs):
        bulbs.append(Bulb(f"{get_local_ip()}{ip_start + i}", effect="sudden"))
        try:
            bulbs[i].start_music()
            if "-v" in sys.argv: print(f"{STR_GREEN_CONSOLE}{bulbs[i]}{STR_NORMAL_CONSOLE}")
            threads.append(threading.Thread(target=tally_task, args=(i+1,), daemon=True))
            threads[i].start()
        except:
            print(f"{STR_YELLOW_CONSOLE}Bulb @ {get_local_ip()}{ip_start + i} unreachable!")
            raise Exception("Error connecting to bulb(s)!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{STR_GREEN_CONSOLE}YeeCue for BM ATEM{STR_NORMAL_CONSOLE} terminated")
        sys.exit()
    except:
        print(f"{STR_YELLOW_CONSOLE}Error connecting to bulbs, terminating...")