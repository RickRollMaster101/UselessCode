#!/usr/bin/python3

import os
import json
import colorama
from colorama import Fore, Back, Style
from sys import platform

colorama.init(autoreset=True)

config = {
   'bashmode': "off",
   'lolcat': "on"
}

login = os.getlogin()
if login == "root":
    login = os.getenv("USER")

linuxconfpath = f'/home/{login}/.config/pyshell'
macconfpath = f'/Users/{login}/.config/pyshell'

if platform == 'linux':
    if os.path.exists(linuxconfpath):
        pass
    else:
        os.mkdir(linuxconfpath)
    if os.path.exists(f'{linuxconfpath}/pyshell-conf.json'):
        pass
    else:
        print(f'{Fore.YELLOW}[+] {Fore.RESET}No config file found, generating config file...')
        with open(f'{linuxconfpath}/pyshell-conf.json', 'a') as f:
            f.write(json.dumps(config))
elif platform == 'darwin':
    if os.path.exists(macconfpath):
        pass
    else:
        os.mkdir(macconfpath)
    if os.path.exists(f'{macconfpath}/pyshell-conf.json'):
        pass
    else:
        print(f'{Fore.YELLOW}[+] {Fore.RESET}No config file found, generating config file...')
        with open(f'{macconfpath}/pyshell-conf.json', 'a') as f:
            f.write(json.dumps(config))



def main():
    if platform == 'linux':
        with open(f'{linuxconfpath}/pyshell-conf.json', 'r') as f:
            config = json.loads(f.read())
    if platform == 'darwin':
        with open(f'{macconfpath}/pyshell-conf.json', 'r') as f:
            config = json.loads(f.read())
    while True:
        print(' ')
        if config['lolcat'] == 'on':
            os.system('whoami|lolcat')
        elif config['lolcat'] == 'off':
            print(login)
        prompt = input("$ ")
        if prompt == 'ls':
            try: 
                print(os.listdir('.'))
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}ls: cannot access')
        elif prompt == 'pwd':
            try:
                print(os.getcwd())
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}pwd: cannot access')
        elif prompt == 'cd':
            try:
                path = input('path: ')
                os.chdir(path)
                print(f'changed directory to {path}')
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}cd: folder not found')
        elif prompt == 'cat':
            try:
                filename = input('filename: ')
                with open(filename, 'r') as f:
                    print(f.read())
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}cat: file not found')
        elif prompt == 'exit':
            print('exiting...')
            exit()
        elif prompt == 'clear':
            os.system('clear')
        elif prompt == 'whoami':
            print(login)
        elif prompt == 'touch':
            try:
                filename = input('filename: ')
                open(filename, 'a').close()
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}touch: cannot create file')
        elif prompt == 'rm':
            try:
                filename = input('filename: ')
                os.remove(filename)
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}rm: cannot remove file')
        elif prompt == 'mkdir':
            try:
                dirname = input('dirname: ')
                os.mkdir(dirname)
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}mkdir: cannot create folder')
        elif prompt == 'rmdir':
            try:
                dirname = input('dirname: ')
                os.rmdir(dirname)
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}rmdir: cannot remove folder')
        elif prompt == 'bash':
            os.system('/bin/bash')
        elif prompt == 'help':
            try:
                print('''Help command for pyshell

    ls		List directory contents
    pwd		Print working directory (aka directory path)
    cd		Change directory
    cat		Print contents of file
    exit	Exit the shell
    clear	Clear the screen
    touch	Make an empty file
    rm		Remove file
    rmdir	Remove directory
    mkdir	Make a directory
    whoami	Prints currently logged in user's username
    bash	Runs bash
    time        Prints the current time
    python      Run a python command
    editconfig  A command for editing the config file
    rmconfig    Deletes the config file
    neofetch    A command-line system information tool by dylanaraps
    help	Show this''')
            except:
                print('help: help file not found')
        elif prompt == 'time':
            print(os.popen('date').read())
        elif prompt == 'python':
            try:
                pycommand = input('command: ')
                exec(pycommand)
            except:
                print(f'{Fore.RED}[x] {Fore.RESET}python: invalid command')
        elif prompt == 'editconfig':
            if platform == 'linux':
                os.system(f'nano {linuxconfpath}/pyshell-conf.json')
            if platform == 'darwin':
                os.system(f'nano {macconfpath}/pyshell-conf.json')
        elif prompt == 'rmconfig':
            if platform == 'linux':
                os.remove(f'{linuxconfpath}/pyshell-conf.json')
            if platform == 'darwin':
                os.remove(f'{macconfpath}/pyshell-conf.json')
        elif prompt == 'neofetch':
            os.system('neofetch --shell_version off | sed "s/zsh/pyshell/g ; s/bash/pyshell/g ; s/fish/pyshell/g"')
        elif prompt == '':
            pass
        else:
            if config['bashmode'] == 'on':
                os.system(prompt)
            elif config['bashmode'] == 'off':
                print(f'{Fore.RED}[x] {Fore.RESET}pyshell: command not found: {prompt} \n{Fore.YELLOW}If you want to run a bash command if the command doesnt exist in pyshell, set bashmode to "{Fore.GREEN}on{Fore.YELLOW}" in ~/.config/pyshell/pyshell-conf.json or by using the "editconfig" command')

if '__main__' == __name__:
    main()

