from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os
import webbrowser
import requests

if os.path.exists('./nitro.png'):
    pass
else:
    nitro = requests.get('https://github.com/RickRollMaster101/UselessCode/blob/main/stuff_for_useless_projects/nitro.png?raw=true')

    open('./nitro.png', 'wb').write(nitro.content)

if os.path.exists('./nitrologo.png'):
    pass
else:
    nitrologo = requests.get('https://github.com/RickRollMaster101/UselessCode/blob/main/stuff_for_useless_projects/nitrologo.png?raw=true')

    open('./nitrologo.png', 'wb').write(nitrologo.content)

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Nitro Gen Hack')
        self.setWindowIcon(QIcon('nitro.png'))
        self.setGeometry(500, 500, 500, 250)
        self.initUI()
        
    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.setText('What nitro do you want?')
        self.label1.move(175, 115)
        self.label1.resize(200, 50)

        self.label = QLabel(self)
        self.pixmap = QPixmap('nitrologo.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(-65, -175)

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
        self.button4.clicked.connect(self.lol)

        self.show()

    def lol(self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Are you sure you want to do this? This is not a joke and can get you banned from discord.')
            msg.setWindowTitle('Confirmation')
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.No)
            retval = msg.exec_()
            if retval == QtWidgets.QMessageBox.Yes:
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            else:
                pass

def window():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

window()