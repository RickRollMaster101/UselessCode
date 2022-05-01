import os
import time
import pyfiglet
import colorama
from colorama import *

colorama.init(autoreset=True)            

def main():
    print(Fore.BLUE + pyfiglet.figlet_format('DDOS TOOL'))
    print(f'{Fore.YELLOW}This tool will attempt to DDOS a person using java ++ c# python++ bash++ c++\n')
    time.sleep(1)
    hacc = input(f'{Fore.RED}Please enter the IP address or the name of the person you want to DDOS: {Fore.YELLOW}')
    time.sleep(1)
    print(f'{Fore.YELLOW}Finding IP for {hacc}......')
    time.sleep(0.2)
    print(f'{Fore.GREEN}Found IP for {hacc}.\n')
    time.sleep(0.2)
    print(f'{Fore.YELLOW}Attempt 1 to DDOS {hacc}\n')
    time.sleep(3)
    print(f'{Fore.RED}Failed\n')
    time.sleep(1)
    print(f'{Fore.YELLOW}Attempt 2 to DDOS {hacc}')
    time.sleep(1)
    print(f'{Fore.GREEN}Success!\n')
    time.sleep(1)
    pings = input(f'{Fore.RED}How many pings to send to {hacc}? {Fore.YELLOW}')
    time.sleep(1.2)
    print(f'{Fore.RED}Flooding {hacc} with {pings} internet packets')
    time.sleep(1)
    i = 0
    pings = int(pings)
    while i < pings:
        print(f'{Fore.YELLOW}Reply from {hacc} 49883880R0JERF9U0QFJERIONINIOPIJ\n')
        time.sleep(0.002)
        print(f'{Fore.YELLOW}Reply from {hacc} 23G809HQ35JP2934JGMRGEWGIO45G8J0\n')
        time.sleep(0.002)
        print(f'{Fore.YELLOW}Reply from {hacc} G89J45G8J049GJRJG90WJERG09WJRGOH\n')
        time.sleep(0.002)
        i += 1
    print(f'{Fore.GREEN}Sent {pings} pings to {hacc}')

if __name__ == '__main__':
    main()