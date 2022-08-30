# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.registerWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.registerWidget.setFont(font)
        self.registerWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.registerWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.registerWidget.setMovable(True)
        self.registerWidget.setObjectName("registerWidget")
        self.uebersicht = QtWidgets.QWidget()
        self.uebersicht.setObjectName("uebersicht")
        self.registerWidget.addTab(self.uebersicht, "")
        self.meischen = QtWidgets.QWidget()
        self.meischen.setObjectName("meischen")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.meischen)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonStop = QtWidgets.QPushButton(self.meischen)
        self.buttonStop.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)
        self.buttonStop.setMinimumSize(QtCore.QSize(100, 100))
        self.buttonStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonStop.setStyleSheet("")
        self.buttonStop.setObjectName("buttonStop")
        self.gridLayout_2.addWidget(self.buttonStop, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 5, 1, 1)
        self.meldungRuehrwerk = QtWidgets.QLabel(self.meischen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meldungRuehrwerk.sizePolicy().hasHeightForWidth())
        self.meldungRuehrwerk.setSizePolicy(sizePolicy)
        self.meldungRuehrwerk.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.meldungRuehrwerk.setFont(font)
        self.meldungRuehrwerk.setText("")
        self.meldungRuehrwerk.setPixmap(QtGui.QPixmap("Icons/Propeller100x100.gif"))
        self.meldungRuehrwerk.setScaledContents(False)
        self.meldungRuehrwerk.setObjectName("meldungRuehrwerk")
        self.gridLayout_2.addWidget(self.meldungRuehrwerk, 0, 1, 1, 1)
        self.meldungHeizplatte = QtWidgets.QLabel(self.meischen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meldungHeizplatte.sizePolicy().hasHeightForWidth())
        self.meldungHeizplatte.setSizePolicy(sizePolicy)
        self.meldungHeizplatte.setMinimumSize(QtCore.QSize(100, 100))
        self.meldungHeizplatte.setText("")
        self.meldungHeizplatte.setPixmap(QtGui.QPixmap("Icons/Heizplatte100x100.png"))
        self.meldungHeizplatte.setScaledContents(False)
        self.meldungHeizplatte.setObjectName("meldungHeizplatte")
        self.gridLayout_2.addWidget(self.meldungHeizplatte, 0, 0, 1, 1)
        self.buttonPlay = QtWidgets.QPushButton(self.meischen)
        self.buttonPlay.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPlay.sizePolicy().hasHeightForWidth())
        self.buttonPlay.setSizePolicy(sizePolicy)
        self.buttonPlay.setMinimumSize(QtCore.QSize(100, 100))
        self.buttonPlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPlay.setMouseTracking(True)
        self.buttonPlay.setStyleSheet("")
        self.buttonPlay.setObjectName("buttonPlay")
        self.gridLayout_2.addWidget(self.buttonPlay, 0, 2, 1, 1)
        self.vertikalTemperaturen = QtWidgets.QVBoxLayout()
        self.vertikalTemperaturen.setObjectName("vertikalTemperaturen")
        self.istTemp = QtWidgets.QLabel(self.meischen)
        self.istTemp.setObjectName("istTemp")
        self.vertikalTemperaturen.addWidget(self.istTemp)
        self.sollTemp = QtWidgets.QLabel(self.meischen)
        self.sollTemp.setObjectName("sollTemp")
        self.vertikalTemperaturen.addWidget(self.sollTemp)
        self.gridLayout_2.addLayout(self.vertikalTemperaturen, 0, 6, 1, 1)
        self.buttonPause = QtWidgets.QPushButton(self.meischen)
        self.buttonPause.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPause.sizePolicy().hasHeightForWidth())
        self.buttonPause.setSizePolicy(sizePolicy)
        self.buttonPause.setMinimumSize(QtCore.QSize(100, 100))
        self.buttonPause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonPause.setStyleSheet("")
        self.buttonPause.setObjectName("buttonPause")
        self.gridLayout_2.addWidget(self.buttonPause, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hinzufuegenB = QtWidgets.QPushButton(self.meischen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hinzufuegenB.sizePolicy().hasHeightForWidth())
        self.hinzufuegenB.setSizePolicy(sizePolicy)
        self.hinzufuegenB.setObjectName("hinzufuegenB")
        self.verticalLayout.addWidget(self.hinzufuegenB)
        self.entfernenB = QtWidgets.QPushButton(self.meischen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entfernenB.sizePolicy().hasHeightForWidth())
        self.entfernenB.setSizePolicy(sizePolicy)
        self.entfernenB.setObjectName("entfernenB")
        self.verticalLayout.addWidget(self.entfernenB)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 6, 1, 1)
        self.rastenTabelle = QtWidgets.QTableWidget(self.meischen)
        self.rastenTabelle.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rastenTabelle.setObjectName("rastenTabelle")
        self.rastenTabelle.setColumnCount(7)
        self.rastenTabelle.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(200, 220, 255))
        self.rastenTabelle.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.rastenTabelle.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.rastenTabelle.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(24)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Feuer200x200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.rastenTabelle.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(150, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsAutoTristate)
        self.rastenTabelle.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/snowflake1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(150, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(200, 220, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.rastenTabelle.setItem(1, 6, item)
        self.gridLayout_2.addWidget(self.rastenTabelle, 1, 0, 1, 6)
        self.registerWidget.addTab(self.meischen, "")
        self.luetern_nachguss = QtWidgets.QWidget()
        self.luetern_nachguss.setObjectName("luetern_nachguss")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.luetern_nachguss)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.registerWidget.addTab(self.luetern_nachguss, "")
        self.kochen = QtWidgets.QWidget()
        self.kochen.setObjectName("kochen")
        self.registerWidget.addTab(self.kochen, "")
        self.einstellungen = QtWidgets.QWidget()
        self.einstellungen.setObjectName("einstellungen")
        self.pushButton = QtWidgets.QPushButton(self.einstellungen)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 201, 61))
        self.pushButton.setObjectName("pushButton")
        self.registerWidget.addTab(self.einstellungen, "")
        self.gridLayout.addWidget(self.registerWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.registerWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerWidget.setTabText(self.registerWidget.indexOf(self.uebersicht), _translate("MainWindow", "Übersicht"))
        self.buttonStop.setText(_translate("MainWindow", "stop"))
        self.buttonPlay.setText(_translate("MainWindow", "play"))
        self.istTemp.setText(_translate("MainWindow", "IST: 30°C"))
        self.sollTemp.setText(_translate("MainWindow", "SOLL: 50°C"))
        self.buttonPause.setText(_translate("MainWindow", "pause"))
        self.hinzufuegenB.setText(_translate("MainWindow", "Hinzufügen"))
        self.entfernenB.setText(_translate("MainWindow", "Entfernen"))
        item = self.rastenTabelle.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.rastenTabelle.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.rastenTabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.rastenTabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temp."))
        item = self.rastenTabelle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dauer"))
        item = self.rastenTabelle.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Typ"))
        item = self.rastenTabelle.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rührer"))
        item = self.rastenTabelle.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Meldung"))
        item = self.rastenTabelle.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Kommentar"))
        __sortingEnabled = self.rastenTabelle.isSortingEnabled()
        self.rastenTabelle.setSortingEnabled(False)
        item = self.rastenTabelle.item(0, 0)
        item.setText(_translate("MainWindow", "anfang"))
        item = self.rastenTabelle.item(0, 4)
        item.setText(_translate("MainWindow", "AN"))
        item = self.rastenTabelle.item(0, 5)
        item.setText(_translate("MainWindow", "AUS"))
        item = self.rastenTabelle.item(1, 0)
        item.setText(_translate("MainWindow", "ende"))
        item = self.rastenTabelle.item(1, 4)
        item.setText(_translate("MainWindow", "AUS"))
        item = self.rastenTabelle.item(1, 5)
        item.setText(_translate("MainWindow", "AN"))
        self.rastenTabelle.setSortingEnabled(__sortingEnabled)
        self.registerWidget.setTabText(self.registerWidget.indexOf(self.meischen), _translate("MainWindow", "Meischen"))
        self.registerWidget.setTabText(self.registerWidget.indexOf(self.luetern_nachguss), _translate("MainWindow", "Leutern/Nachguss"))
        self.registerWidget.setTabText(self.registerWidget.indexOf(self.kochen), _translate("MainWindow", "Kochen"))
        self.pushButton.setText(_translate("MainWindow", "Brauruf Test"))
        self.registerWidget.setTabText(self.registerWidget.indexOf(self.einstellungen), _translate("MainWindow", "Einstellungen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
