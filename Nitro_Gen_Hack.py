from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QImage
import sys
import os
import webbrowser
import requests
import pyfiglet
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Nitro Gen Hack')
        self.setGeometry(500, 500, 500, 250)
        self.initUI()
        
    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.setText('What nitro do you want?')
        self.label1.move(175, 115)
        self.label1.resize(200, 50)

        image_url = 'https://github.com/RickRollMaster101/UselessCode/blob/main/stuff_for_useless_projects/nitrologo.png?raw=true'

        self.image = QImage()
        self.image.loadFromData(requests.get(image_url).content)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap.fromImage(self.image))
        self.image_label.resize(self.image.width(),
                                self.image.height())
        self.image_label.move(-65, -175)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Exit')
        self.button1.clicked.connect(self.close)
        self.button1.move(200, 185)

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText('Nitro Boost')
        self.button3.move(50, 185)
        self.button3.clicked.connect(self.lol)

        self.button4 = QtWidgets.QPushButton(self)
        self.button4.setText('Nitro Classic')
        self.button4.move(350, 185)
        self.button4.clicked.connect(self.lol2)

        self.show()

    def lol(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('This is not a joke and can get you banned from discord. Are you sure you want to do this?')
            msg.setWindowTitle('Confirmation')
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            retval = msg.exec_()
            if retval == QtWidgets.QMessageBox.Yes:
                print(Fore.BLUE + pyfiglet.figlet_format('Modifying client', font='slant'))
                print('This will take a bit of time')
                time.sleep(1.5)
                print(f'{Fore.YELLOW}Patching "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/IfHaveNitro.js"')
                time.sleep(1)
                print(f'{Fore.YELLOW}Setting "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/IfHaveNitro.js" to {Fore.GREEN}True')
                time.sleep(1)
                print(f'{Fore.YELLOW}Adding file "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/Nitro/NitroBoost.js"')
                time.sleep(5)
                print(Fore.GREEN + pyfiglet.figlet_format('Done!'))
                print(f'{Fore.RED}You will need to reopen discord for you to receive the nitro')
                done = QtWidgets.QMessageBox()
                done.setIcon(QtWidgets.QMessageBox.Information)
                done.setText('You will need to reopen discord for you to receive the nitro')
                done.setWindowTitle('Done!')
                done.setStandardButtons(QtWidgets.QMessageBox.Ok)
                done.setDefaultButton(QtWidgets.QMessageBox.Ok)
                retval = done.exec_()
                if retval == QtWidgets.QMessageBox.Ok:
                    pass
                time.sleep(2)
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                time.sleep(10)
                nohacc = QtWidgets.QMessageBox()
                nohacc.setIcon(QtWidgets.QMessageBox.Information)
                nohacc.setText('<h3>Get RICKROLLED!, Dont worry you didnt get hacked</h3><a href="https://github.com/RickRollMaster101/UselessCode/blob/main/Nitro_Gen_Hack.py">Source</a>')
                nohacc.setWindowTitle('Rickrolled!')
                nohacc.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = nohacc.exec_()
                if retval == QtWidgets.QMessageBox.Ok:
                    pass

    def lol2(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('This is not a joke and can get you banned from discord. Are you sure you want to do this?')
            msg.setWindowTitle('Confirmation')
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            retval = msg.exec_()
            if retval == QtWidgets.QMessageBox.Yes:
                print(Fore.BLUE + pyfiglet.figlet_format('Modifying client', font='slant'))
                print('This will take a bit of time')
                time.sleep(1.5)
                print(f'{Fore.YELLOW}Patching "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/IfHaveNitro.js"')
                time.sleep(1)
                print(f'{Fore.YELLOW}Setting "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/IfHaveNitro.js" to {Fore.GREEN}True')
                time.sleep(1)
                print(f'{Fore.YELLOW}Adding file "C:/Users/{os.getlogin()}/AppData/Local/Packages/Discord/0.0.1-stable/resources/app/Nitro/NitroClassic.js"')
                time.sleep(5)
                print(Fore.GREEN + pyfiglet.figlet_format('Done!'))
                print(f'{Fore.RED}You will need to reopen discord for you to receive the nitro')
                done = QtWidgets.QMessageBox()
                done.setIcon(QtWidgets.QMessageBox.Information)
                done.setText('You will need to reopen discord for you to receive the nitro')
                done.setWindowTitle('Done!')
                done.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = done.exec_()
                if retval == QtWidgets.QMessageBox.Ok:
                    pass
                time.sleep(2)
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                time.sleep(10)
                nohacc = QtWidgets.QMessageBox()
                nohacc.setIcon(QtWidgets.QMessageBox.Information)
                nohacc.setText('<h3>Get RICKROLLED!, Dont worry you didnt get hacked</h3><a href="https://github.com/RickRollMaster101/UselessCode/blob/main/Nitro_Gen_Hack.py">Source</a>')
                nohacc.setWindowTitle('Rickrolled!')
                nohacc.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = nohacc.exec_()
                if retval == QtWidgets.QMessageBox.Ok:
                    pass


def window():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

window()