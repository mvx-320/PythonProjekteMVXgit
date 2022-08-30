# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import form

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()


    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

def clicked():
    print("Deine Mudder stinkt")

if __name__ == "__main__":
#    app = QApplication([])
 #   widget = MainWindow()
  #  widget.show()
   # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = form.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(clicked)
    MainWindow.show()
    sys.exit(app.exec_())