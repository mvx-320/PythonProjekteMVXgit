# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogNeueRast.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NeueRastHinzufuegen(object):
    def setupUi(self, NeueRastHinzufuegen):
        NeueRastHinzufuegen.setObjectName("NeueRastHinzufuegen")
        NeueRastHinzufuegen.setEnabled(True)
        NeueRastHinzufuegen.resize(935, 603)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Brauerei1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NeueRastHinzufuegen.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(NeueRastHinzufuegen)
        self.gridLayout.setObjectName("gridLayout")
        self.braurufChB = QtWidgets.QCheckBox(NeueRastHinzufuegen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.braurufChB.sizePolicy().hasHeightForWidth())
        self.braurufChB.setSizePolicy(sizePolicy)
        self.braurufChB.setMinimumSize(QtCore.QSize(0, 7))
        self.braurufChB.setStyleSheet("QCheckBox::indicator{width: 25px; height: 25px; };")
        self.braurufChB.setText("")
        self.braurufChB.setObjectName("braurufChB")
        self.gridLayout.addWidget(self.braurufChB, 5, 1, 1, 1)
        self.positionCoB = QtWidgets.QComboBox(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.positionCoB.setFont(font)
        self.positionCoB.setObjectName("positionCoB")
        self.positionCoB.addItem("")
        self.positionCoB.addItem("")
        self.positionCoB.addItem("")
        self.positionCoB.addItem("")
        self.gridLayout.addWidget(self.positionCoB, 0, 1, 1, 1)
        self.ruehrwerkL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ruehrwerkL.setFont(font)
        self.ruehrwerkL.setObjectName("ruehrwerkL")
        self.gridLayout.addWidget(self.ruehrwerkL, 4, 0, 1, 1)
        self.dialogButtons = QtWidgets.QDialogButtonBox(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dialogButtons.setFont(font)
        self.dialogButtons.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtons.setObjectName("dialogButtons")
        self.gridLayout.addWidget(self.dialogButtons, 8, 0, 1, 2)
        self.temperaturLE = QtWidgets.QLineEdit(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.temperaturLE.setFont(font)
        self.temperaturLE.setFrame(True)
        self.temperaturLE.setObjectName("temperaturLE")
        self.gridLayout.addWidget(self.temperaturLE, 2, 1, 1, 1)
        self.dauerLE = QtWidgets.QLineEdit(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dauerLE.setFont(font)
        self.dauerLE.setObjectName("dauerLE")
        self.gridLayout.addWidget(self.dauerLE, 3, 1, 1, 1)
        self.temperatorL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.temperatorL.setFont(font)
        self.temperatorL.setObjectName("temperatorL")
        self.gridLayout.addWidget(self.temperatorL, 2, 0, 1, 1)
        self.bezeichnungLE = QtWidgets.QLineEdit(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.bezeichnungLE.setFont(font)
        self.bezeichnungLE.setObjectName("bezeichnungLE")
        self.gridLayout.addWidget(self.bezeichnungLE, 1, 1, 1, 1)
        self.ruehrwerkChB = QtWidgets.QCheckBox(NeueRastHinzufuegen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ruehrwerkChB.sizePolicy().hasHeightForWidth())
        self.ruehrwerkChB.setSizePolicy(sizePolicy)
        self.ruehrwerkChB.setMinimumSize(QtCore.QSize(704, 38))
        self.ruehrwerkChB.setSizeIncrement(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ruehrwerkChB.setFont(font)
        self.ruehrwerkChB.setStyleSheet("QCheckBox::indicator{width: 25px; height: 25px; };")
        self.ruehrwerkChB.setText("")
        self.ruehrwerkChB.setObjectName("ruehrwerkChB")
        self.gridLayout.addWidget(self.ruehrwerkChB, 4, 1, 1, 1)
        self.bezeichnungL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.bezeichnungL.setFont(font)
        self.bezeichnungL.setObjectName("bezeichnungL")
        self.gridLayout.addWidget(self.bezeichnungL, 1, 0, 1, 1)
        self.braurufL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.braurufL.setFont(font)
        self.braurufL.setObjectName("braurufL")
        self.gridLayout.addWidget(self.braurufL, 5, 0, 1, 1)
        self.positionL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.positionL.setFont(font)
        self.positionL.setObjectName("positionL")
        self.gridLayout.addWidget(self.positionL, 0, 0, 1, 1)
        self.kommentarTE = QtWidgets.QTextEdit(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.kommentarTE.setFont(font)
        self.kommentarTE.setObjectName("kommentarTE")
        self.gridLayout.addWidget(self.kommentarTE, 6, 1, 1, 1)
        self.kommentarL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.kommentarL.setFont(font)
        self.kommentarL.setObjectName("kommentarL")
        self.gridLayout.addWidget(self.kommentarL, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 2)
        self.dauerL = QtWidgets.QLabel(NeueRastHinzufuegen)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dauerL.setFont(font)
        self.dauerL.setObjectName("dauerL")
        self.gridLayout.addWidget(self.dauerL, 3, 0, 1, 1)

        self.retranslateUi(NeueRastHinzufuegen)
        self.dialogButtons.accepted.connect(NeueRastHinzufuegen.accept)
        self.dialogButtons.rejected.connect(NeueRastHinzufuegen.reject)
        QtCore.QMetaObject.connectSlotsByName(NeueRastHinzufuegen)

    def retranslateUi(self, NeueRastHinzufuegen):
        _translate = QtCore.QCoreApplication.translate
        NeueRastHinzufuegen.setWindowTitle(_translate("NeueRastHinzufuegen", "Neue Rast hinzufügen"))
        self.positionCoB.setItemText(0, _translate("NeueRastHinzufuegen", "1"))
        self.positionCoB.setItemText(1, _translate("NeueRastHinzufuegen", "2"))
        self.positionCoB.setItemText(2, _translate("NeueRastHinzufuegen", "3"))
        self.positionCoB.setItemText(3, _translate("NeueRastHinzufuegen", "4"))
        self.ruehrwerkL.setText(_translate("NeueRastHinzufuegen", "Rührwerk:"))
        self.temperatorL.setText(_translate("NeueRastHinzufuegen", "Temperatur:"))
        self.bezeichnungL.setText(_translate("NeueRastHinzufuegen", "Bezeichnung:"))
        self.braurufL.setText(_translate("NeueRastHinzufuegen", "Brauruf:"))
        self.positionL.setText(_translate("NeueRastHinzufuegen", "Rast an Position:"))
        self.kommentarL.setText(_translate("NeueRastHinzufuegen", "Kommentar:"))
        self.dauerL.setText(_translate("NeueRastHinzufuegen", "Dauer:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NeueRastHinzufuegen = QtWidgets.QDialog()
    ui = Ui_NeueRastHinzufuegen()
    ui.setupUi(NeueRastHinzufuegen)
    NeueRastHinzufuegen.show()
    sys.exit(app.exec_())
