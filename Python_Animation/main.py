from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from pyside6_loader import PySide6Ui

# evtl. zum Umwandeln .ui zu .py im Programm

#   from PySide6.QtUiTools import QUiLoader
#   loader = QUiLoader()


# Compile ui file
PySide6Ui('main_gui.ui').toPy()

# from PyQt6.Widgets import QApplication, QWidget
## pyuic6 main_gui.ui -o main_gui.py

import main_gui

#class App2(QWidget):
#   def __init__(self):
#        QWidget.__init__(self)
#        self.ui2 = main_gui.Ui_JumpingButtons()
#        self.ui2.setupUi(self)

class App1(QWidget):
    def __int__(self):
        QMainWindow.__init__(self)
     #   QMainWindow.setCentralWidget(App2)
        self.ui1 = main_gui.Ui_JumpButtons()
        self.ui1.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QApplication([])
    app2 = QWidget
    window = App1()
#    cwigdet = App2()
#    window.setCentralWidget(cwigdet)
    window.show()
    exit(app.exec())