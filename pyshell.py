import os

def main():
    while True:
        print(' ')
        os.system('whoami|lolcat')
        prompt = input("$ ")
        if prompt == 'ls':
            print(os.listdir('.'))
        elif prompt == 'pwd':
            print(os.getcwd())
        elif prompt == 'cd':
            path = input('path: ')
            os.chdir(path)
            print(f'changed directory to {path}')
        elif prompt == 'cat':
            filename = input('filename: ')
            with open(filename, 'r') as f:
                print(f.read())
        elif prompt == 'exit':
            print('exiting...')
            exit()
        elif prompt == 'clear':
            os.system('clear')
        elif prompt == 'whoami':
            print(os.getlogin())
        elif prompt == 'touch':
            filename = input('filename: ')
            open(filename, 'a').close()
        elif prompt == 'rm':
            filename = input('filename: ')
            os.remove(filename)
        elif prompt == 'mkdir':
            dirname = input('dirname: ')
            os.mkdir(dirname)
        elif prompt == 'rmdir':
            dirname = input('dirname: ')
            os.rmdir(dirname)
        elif prompt == 'bash':
            os.system('/bin/bash')
        elif prompt == 'help':
            with open('./stuff_for_useless_projects/help', 'r') as f:
                print(f.read())
        else:
            print(f'pyshell: command not found: {prompt}')

if '__main__' == __name__:
    main()
