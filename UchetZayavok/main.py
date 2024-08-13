from PyQt5.QtWidgets import (
    QApplication,
    QDialog 
)
from PyQt5.uic import loadUi

import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui  import QPixmap, QIcon


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
icon = QIcon()
icon.addPixmap(QPixmap("logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon) 
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")