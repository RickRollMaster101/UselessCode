import os, sys, time
import webbrowser
import pyfiglet
import random
import gdown

if len(sys.argv) > 1:
    command = sys.argv[1].lower()
else:
    command = print('Please enter an arguement')


if command == 'help':
    print('No one will be using this anyway so no useful help command')
elif command == 'beluga':
    os.system('clear')
    pyfiglet.print_figlet('HECKING BELUGA!!!!!!!!!!!!!!')
    time.sleep(3)
    os.system('clear')
    pyfiglet.print_figlet('FAILED.')
    print('ERR: WINDOWS_DEFENDER_ON_MAC')
    print('Abort.')
elif command == 'stop':
    print('Stopping...')
    os.abort()
elif command == 'airstrike':
    webbrowser.open('https://youtu.be/MaJQxVkeiJg?t=28')
elif command == 'bank':
    os.system('clear')
    pyfiglet.print_figlet('Ballence: $0.65')
    money = input('Enter the amount of money you want: ')
    os.system('clear')
    pyfiglet.print_figlet(f'Ballence: ${money}')
    time.sleep(3)
elif command == 'earth':
    pyfiglet.print_figlet('hecking earth.....')
    open('./heckcheck/earthhecked', 'a').close()
    time.sleep(3)
    pyfiglet.print_figlet('hecked earth')
elif command == 'create_earthquake':
    if os.path.exists('./heckcheck/earthhecked'):
        webbrowser.open('https://youtu.be/MaJQxVkeiJg?t=73')
    else:
        print('ERR: EARTH_NOT_HECKED')
elif command == 'meteor':
    webbrowser.open('https://youtu.be/MaJQxVkeiJg?t=84')
elif command == 'e':
    e = ['https://youtu.be/MaJQxVkeiJg?t=125', 'https://youtu.be/MaJQxVkeiJg?t=131', 'https://youtu.be/MaJQxVkeiJg?t=133']
    webbrowser.open(random.choice(e))
