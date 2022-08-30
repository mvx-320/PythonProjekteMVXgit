import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import time # für QDateTimeEdit

# Bei QTCreator: Preview (Alt; Umsch; R) oder Extras -> Formulareditor -> Vorschau...

# Größe der Bauteile selbst zuweisen sonst kann sie sich im nachhinein verändern

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'): # Man kann das auch mit anderen datein machen zb txt (für die Datenbank später
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Fenster (QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

#        # TabWidgets einfach beim QTCreator einfügen
#        self.tab1 = QWidget()
#        self.tab2 = QWidget()
#
#        self.addTab(self.tab1, "Tab1")
#        self.addTab(self.tab2, "Tab2")

        box = QVBoxLayout(self)
        self.setLayout(box)



#        # QGridLayout: Layout mit dem man Gleichförmige Boxen erstellen kann
#        grid = QGridLayout()
#        namen = ['1', '2', '3', '4', '5', '6',]
#        posis = [(i,j) for i in range(3) for j in range(2)]
#        for pos, name in zip (posis, namen):
#            button = QPushButton(name)
#            grid.addWidget(button, *pos)

        w = QLabel(self)
        w.setText("<a href='https://www.google.com'>google</a>")
        w.setOpenExternalLinks(True)
        w.linkActivated.connect(self.clicked) # linkHovered wenn man nur mit der Maus darüber fährt
        w.move(50, 50)

        c = QCheckBox("Check me out", self)
        c.move(50, 100)
#        c.toggle() # Lässt eine CheckBox von selbst togglen
        c.stateChanged.connect(self.clicked)

        # Gibt es auch als QRadioButton (der wird aber mit toggled angesteuert)
        # CheckBox rechteckig, RadioButton rund

        p = QPushButton("Drück mich fest", self)
        p.setCheckable(True) # Nicht sicher für was der ist
        p.move(50, 150)
        p.clicked[bool].connect(self.clicked) # Macht den Button togglebar

        self.co = QComboBox(self) # co muss eine Variable der Klasse werden damit man sie in clicked2 aufrufen kann
        self.co.move(50,200)
        self.co.addItem("Java")
        self.co.addItems(["C#", "Rust", "Hacken"])
        self.co.currentIndexChanged.connect(self.clicked2)

        self.spin = QSpinBox(self)
        self.spin.setGeometry(50, 250, 100, 20) # lässt so trotzdem keine größeren Werte als 99 zu + Eingabe erst bei Enter abfragen
        self.spin.valueChanged.connect(self.clicked3)

        self.slider = QSlider(self)
        self.slider.move(50,300)
        self.slider.sliderReleased.connect(self.clicked4)
        self.slider.setMinimum(50)
        self.slider.setMaximum(1000)
        self.slider.setValue(250)

        self.line = QLineEdit(self) # Es gäbe noch QTextEdit für einen größeren Textbereich (Stürzt wegen dem Übergabeparameter bei textChanged ab) (außerdem wird so textChanged garnicht verwendet, sondern in der Methode mit toPlainText() auf den Text zugegriffen (muss dann allerdings noch mit str() geparst werden)
        self.line.move(300,50)
        self.line.textChanged.connect(self.clicked5) # Hier sollte man noch eine extra Abfrage für z.B die Enter-Taste einfügen
#        self.line.setValidator(QDoubleValidator()) # Lässt nur Zahlen eingeben
#        self.line.setInputMask("999.99") # Setzt eine Maske auf das Eingabefeld
#        self.line.setEchoMode(QLineEdit.Password) # Verbirgt die Eingabe (für Passwörter)
#        self.line.setReadOnly(True) # Damit kann man nichts rein schreiben (MACHT KEINEN SINN)

        self.progress = QProgressBar(self)
        self.timer = QBasicTimer()
        self.i = 0
        self.timer.start(100, self)
        self.progress.move(300, 100)

        self.calender = QCalendarWidget(self)
        self.calender.move(300,150)
        self.calender.clicked.connect(self.clicked6)

        self.lcdNr = QLCDNumber(self) # SPIELEREI Zeigt Zahlen an wie ein digitaler Wecker
        self.lcdNr.setGeometry(550,50,250,35)
        self.lcdNr.setNumDigits(20)
        self.lcdNr.display("00:15 16.18.2022")

        self.dateT = QDateTimeEdit(self)
        self.dateT.move(550, 100)
        now = QDateTime()
        now.setTime_t(int(time.time()))
        self.dateT.setDateTime(now)
        self.dateT.dateTimeChanged.connect(self.clicked6) # Geht auch nur als dateChanged bzw. timeChanged

        edit = QLineEdit('Drag me', self)
        edit.setDragEnabled(True)
        edit.move(870, 50)
        btn = Button('Drop it on me', self)
        btn.move(870, 100)


####### Dialogfenster

        self.fontBu = QPushButton("Schriftart wechseln", self) # Font Dialog
        self.fontBu.move(750,100)
        self.fontBu.clicked.connect(self.clicked7)

        self.fileBu = QPushButton("Wähle ein Bild", self) # File Dialog
        self.fileBu.move(750,150)
        self.fileBu.clicked.connect(self.clicked8)
        self.picLa = QLabel("Ich werde ein Bild", self)
        self.picLa.setGeometry(750,200,200,200)

        self.colorBu = QPushButton("Wähle eine Hintergrundfarbe", self) # Color Dialog
        self.colorBu.move(750,400)
        self.colorBu.clicked.connect(self.clicked9)

        self.inputBu = QPushButton("Schreibe eine Input", self) # Input Dialog
        self.inputBu.move(750,450)
        self.inputBu.clicked.connect(self.clickedA)




#        self.setLayout(grid) # Für das Grid Layout
        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Firestater")
        self.setWindowIcon(QIcon("Icons\\Feuer1200x1200.png"))
        self.show()

    def clicked(self, down):
        # Wird ausgeführt wenn setOpenExternalLinks = False
        #print("gedrückt")

        if down:
            print("down")
        else:
            print("up")

    def clicked2(self, i):
        print(self.co.currentText())
        print(i) # Geht auch ohne Übergabeparameter mit .currentIndex

    def clicked3(self):
        print(self.spin.value())

    def clicked4(self):
        print(self.slider.value())

    def clicked5(self, text):
        print(text)

    def timerEvent(self, e):
        if self.i >= 100:
            self.timer.stop()
        self.i = self.i + 1
        self.progress.setValue(self.i)

    def clicked6(self, date):
        print(date.toString())

    def clicked7(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.fontBu.setFont(font)

    def clicked8(self):
        fd =QFileDialog()
        fname = fd.getOpenFileName(self, 'Datei öffnen', 'C:\\Users\\max0t\\OneDrive\\Dokumente\\PythonProjekteMVX\\untitled1\\Icons',
                                   "Nur Bilddateien einfügen (*.jpg *.png") # In die letzte Klammer nur die Dateitypen
        self.picLa.setPixmap(QPixmap(fname[0]))

    def clicked9(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet("QWidget {background-color: %s }" % color.name()) # Setzt den Gesamthintergrund auf die gewählte Farbe

    def clickedA(self):
        text, ok = QInputDialog.getText(self, 'Wie ist dein Name?', 'Gib deinen Namen ein!', False, 'Los mach!!') # Hier ist True und False nicht angebracht

        if ok:
            print(text)

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())