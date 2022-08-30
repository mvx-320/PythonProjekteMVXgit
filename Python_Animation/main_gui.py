# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from myWidgets import JumpButton

class Ui_JumpingButtons(object):
    def setupUi(self, JumpingButtons):
        if not JumpingButtons.objectName():
            JumpingButtons.setObjectName(u"JumpingButtons")
        JumpingButtons.resize(1920, 1080)
        JumpingButtons.setLayoutDirection(Qt.LeftToRight)
        JumpingButtons.setStyleSheet(u"QPushButton{\n"
"	border:5px solid rgb(25,50,55)\n"
"}")
        self.pushButton = JumpButton(JumpingButtons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 160, 291, 161))
        font = QFont()
        font.setFamilies([u"Siemens Serif"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.retranslateUi(JumpingButtons)

        QMetaObject.connectSlotsByName(JumpingButtons)
    # setupUi

    def retranslateUi(self, JumpingButtons):
        JumpingButtons.setWindowTitle(QCoreApplication.translate("JumpingButtons", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("JumpingButtons", u"PushButton", None))
    # retranslateUi

