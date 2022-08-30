from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import ui1, dialogRast

# Rast Hinzufügen Button gedrückt
def rastHinzufuegen():
    NeueRastHinzufuegen.show()

   # ranz.dialogAuslesen()

# Test um GitHub zu verstehen123

# Rast Enfernen Button gedrückt
def rastEntfernen():
    print("Dreckssack")



class Dialog:
    @staticmethod
    def dialogAuslesen():
        position = dialog.positionCoB.currentIndex()
        bezeichnung = dialog.bezeichnungLE.text()
        temperatur = int(dialog.temperaturLE.text())
        pass

class Rast:
    #ID = 0

    def __init__(self, name, temp, time, typ, agitator, brauruf, comment):
        self.name = str(name)
        self.temp = int(temp)
        self.time = int(time)
        self.typ = int(typ)
        self.agitator = bool(agitator)
        self.brauruf = bool(brauruf)
        self.comment = str(comment)
        self.ID += 1 # Passt so noch nicht. Muss noch auf position angepasst werden

    # private Variablen evtl. durch Keyword @property
    # getter- / setter-Methoden
    # Sicherheit (private) (unsichere Methode __Name (für Variablen & Funktionen)
    # nur bestimmten Datentyp annehmen

    def RührwerkAn(self):
        # Ausgangsbeschaltung des Raspberrys
        pass

def chanceMainWindow():
    ui.rastenTabelle.setColumnWidth(0, 300)
    ui.rastenTabelle.setColumnWidth(1, 50)
    ui.rastenTabelle.setColumnWidth(2, 60)
    ui.meldungRuehrwerk.setMovie(movie)
    movie.start()

def chanceDialog():
#!!!!! Größe vom Dialogfenster wieder veränderbar machen
#!!!!! Hier muss noch rein das die ComboBox nur soviele Zahlen hat wie es auch rows gibt
    dialog.positionCoB.setCurrentIndex(ui.rastenTabelle.rowCount())
#!!!!! Die aktuellen Lehrzeichen müssen entfernt werden
    dialog.temperaturLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.temperaturLE.setInputMask("00") #D damit die Zahl >0 sein muss
    dialog.dauerLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.dauerLE.setInputMask("000")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ui1.Ui_MainWindow()
ui.setupUi(MainWindow)

movie = QtGui.QMovie("Icons\\one_peace.gif")
movie.setScaledSize(QtCore.QSize(100, 100))

chanceMainWindow()


NeueRastHinzufuegen = QtWidgets.QDialog()
dialog = dialogRast.Ui_NeueRastHinzufuegen()
dialog.setupUi(NeueRastHinzufuegen)
chanceDialog()

ui.hinzufuegenB.clicked.connect(rastHinzufuegen)    # .connect darf nicht in die Methode verschoben werden
ui.entfernenB.clicked.connect(rastEntfernen)

dialogC = Dialog()
dialog.dialogButtons.clicked.connect(lambda: dialogC.dialogAuslesen())







MainWindow.show()
sys.exit(app.exec_())