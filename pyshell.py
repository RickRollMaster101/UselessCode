import os

def main():
    while True:
        print(' ')
        os.system('whoami|lolcat')
        prompt = input("$ ")
        if prompt == 'ls':
            try: 
                print(os.listdir('.'))
            except:
                print('ls: cannot access')
        elif prompt == 'pwd':
            try:
                print(os.getcwd())
            except:
                print('pwd: cannot access')
        elif prompt == 'cd':
            try:
                path = input('path: ')
                os.chdir(path)
                print(f'changed directory to {path}')
            except:
                print('cd: folder not found')
        elif prompt == 'cat':
            try:
                filename = input('filename: ')
                with open(filename, 'r') as f:
                    print(f.read())
            except:
                print('cat: file not found')
        elif prompt == 'exit':
            print('exiting...')
            exit()
        elif prompt == 'clear':
            os.system('clear')
        elif prompt == 'whoami':
            print(os.getlogin())
        elif prompt == 'touch':
            try:
                filename = input('filename: ')
                open(filename, 'a').close()
            except:
                print('touch: cannot create file')
        elif prompt == 'rm':
            try:
                filename = input('filename: ')
                os.remove(filename)
            except:
                print('rm: cannot remove file')
        elif prompt == 'mkdir':
            try:
                dirname = input('dirname: ')
                os.mkdir(dirname)
            except:
                print('mkdir: cannot create folder')
        elif prompt == 'rmdir':
            try:
                dirname = input('dirname: ')
                os.rmdir(dirname)
            except:
                print('rmdir: cannot remove folder')
        elif prompt == 'bash':
            os.system('/bin/bash')
        elif prompt == 'help':
            try:
                with open('./stuff_for_useless_projects/help', 'r') as f:
                    print(f.read())
            except:
                print('help: help file not found')
        elif prompt == 'time':
            print(os.popen('date').read())
        elif prompt == 'python':
            try:
                pycommand = input('command: ')
                exec(pycommand)
            except:
                print('python: invalid command')
        else:
            print(f'pyshell: command not found: {prompt}')

if '__main__' == __name__:
    main()

