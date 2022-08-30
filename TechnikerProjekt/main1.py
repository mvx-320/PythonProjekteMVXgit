# Thisbrauruf=None Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Strg+F8 to toggle the breakpoint. (Use a breakpoint in the code line below to debug your script.)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtBoundSignal
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

import sys
import time

import UI1


# Rast Hinzufügen Button gedrückt
def rastHinzufuegen(self):
    print("test")


# Rast Enfernen Button gedrückt
def rastEntfernen(self):
    pass


def uiCodeAEnderungen():
    ui.rastenTabelle.setColumnWidth(0, 300)
    ui.rastenTabelle.setColumnWidth(1, 50)
    ui.rastenTabelle.setColumnWidth(2, 60)
    ui.hinzufuegenB.clicked.connected(rastHinzufuegen)

    ui.meldungRuehrwerk.setMovie(movie)
    movie.start()


app = QtWidgets.QApplication(sys.argv)
movie = QtGui.QMovie("Icons\\Propeller2.gif")
movie.setScaledSize(QtCore.QSize(100, 100))

MainWindow = QtWidgets.QMainWindow()
ui = UI1.Ui_MainWindow()
ui.setupUi(MainWindow)
uiCodeAEnderungen()

MainWindow.show()
sys.exit(app.exec_())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Import für später (from [Dateiname] import ...)
# Um die Registerseite zu wechseln self.registerWidget.setCurrentIndex(1)

# Neues (Header-)Item ins tableWidget:
#  und wichtig setRowCount(+1)
#   self.tableWidget.setVerticalHeaderItem(2, QtWidgets.QTableWidgetItem())
#   self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem())
# in retranslateUi
#   self.tableWidget.verticalHeaderItem(2).setText(_translate("MainWindow", "3"))
#   self.tableWidget.item(2, 0).setText(_translate("MainWindow", "nrDrei"))

class Rast:
    ID = 0

    def __init__(self, name, temp, time, brauruf=False):
        self.name = name
        self.temp = temp
        self.time = time
        self.brauruf = brauruf
        self.ID += 1

    # private Variablen evtl. durch Keyword @property
    # getter- / setter-Methoden
    # Sicherheit (private) (unsichere Methode __Name (für Variablen & Funktionen)
    # nur bestimmten Datentyp annehmen

    def RührwerkAn(self):
        # Ausgangsbeschaltung des Raspberrys
        pass


rast1 = Rast.__init__("hans", 10, 20, True)

# Schrittkette
#       Hier muss ein eigener Thread eingefügt werden

step = 0
