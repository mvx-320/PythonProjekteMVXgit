# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImagesWithQPixMap1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 400, 400))
        #self.label.setAutoFillBackground(True)
        #self.label.setStyleSheet("color: rgba(0, 0, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/Heizung1_gruen.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.heizungEIN = QtWidgets.QPushButton(self.centralwidget)
        self.heizungEIN.setGeometry(QtCore.QRect(500, 100, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Siemens Sans Black")
        font.setPointSize(18)
        font.setItalic(True)
        font.setUnderline(True)
        self.heizungEIN.setFont(font)
        self.heizungEIN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heizungEIN.setMouseTracking(False)
        self.heizungEIN.setAutoDefault(False)
        self.heizungEIN.setDefault(False)
        self.heizungEIN.setFlat(False)
        self.heizungEIN.setObjectName("heizungEIN")
        self.heizungAUS = QtWidgets.QPushButton(self.centralwidget)
        self.heizungAUS.setGeometry(QtCore.QRect(500, 300, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Siemens Slab")
        font.setPointSize(20)
        font.setStrikeOut(True)
        self.heizungAUS.setFont(font)
        self.heizungAUS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heizungAUS.setObjectName("heizungAUS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heizungEIN.setText(_translate("MainWindow", "Heizung EIN"))
        self.heizungAUS.setText(_translate("MainWindow", "Heizung AUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
