from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

import main
import ui1, dialogRast

# Rast Hinzufügen Button gedrückt
def rastHinzufuegen():
    #!!!! letzte Rastposition an das DialogFenster übergeben

    main.currentID = ui.rastenTabelle.rowCount() +1
    dialog.positionCoB.clear()
    for i in range(main.currentID):
        dialog.positionCoB.addItem(str(i+1))
    dialog.positionCoB.setCurrentIndex(main.currentID -1)
    dialog.bezeichnungLE.clear()
    dialog.temperaturLE.clear()
    dialog.dauerLE.clear()
    dialog.typCoB.setCurrentIndex(0)
    dialog.ruehrwerkChB.setCheckState(0)
    dialog.braurufChB.setCheckState(0)
    dialog.kommentarTE.clear()

    NeueRastHinzufuegen.show()

    #ui.rastenTabelle.setRowCount(3) # muss größer werden

    #!!!!!!! Abchecken ob man neues VericalItem erzeugen muss

   # ranz.dialogAuslesen()


# Rast Enfernen Button gedrückt
def rastEntfernen():
    #!!!! Nachfrage 'Soll die Rast wirklich gelöscht werden?'
    print("Dreckssack\n alsdjföl")


class Dialog:
    @staticmethod
    def dialogAuslesen():


        main.currentID = dialog.positionCoB.currentIndex() +1
        bezeichnung = dialog.bezeichnungLE.text()
        temperatur = dialog.temperaturLE.text()
        dauer = dialog.dauerLE.text()
        typ = dialog.typCoB.currentIndex()
        if dialog.ruehrwerkChB.checkState() == 2: # 0 = Unchecked; 2 = Checked
            ruehrwerk = True
        else:
            ruehrwerk = False
        if dialog.braurufChB.checkState() == 2:
            brauruf = True
        else:
            brauruf = False
        kommentar = dialog.kommentarTE.document().toPlainText()
        kommentar = kommentar.replace('\n','  ')
        #       print(main.currentID)
        #       print(rasten_array.count(0))
        if main.currentID > len(rasten_array) +1:
            main.currentID = len(rasten_array) +1
        if main.currentID < 1:
            main.currentID = 1
        #       print(ruehrwerk)
        rasten_array.insert(main.currentID - 1,Rast(bezeichnung, str(kommentar), temperatur, dauer, typ, ruehrwerk, brauruf))

        # nur zum testen
#        for i in range(0, len(rasten_array)):
 #           print(main.currentID)
  #          print(i)
   #         print(rasten_array[i].name)

        Dialog.tabelleAktualisieren()

    @staticmethod
    def tabelleAktualisieren():
        _translate = QtCore.QCoreApplication.translate
        ui.rastenTabelle.setRowCount(len(rasten_array))
        for i in range(len(rasten_array)):
            ui.rastenTabelle.setRowHeight(i, 50)

        for h in range(0, len(rasten_array)):
            print(h)
            for i in range(ui.rastenTabelle.columnCount()):
                item = QtWidgets.QTableWidgetItem()

                # Blaufärbung bei jeder 2. Zeile
                if h % 2 == 0:
                    brush = QtGui.QBrush(QtGui.QColor(240, 240, 255))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

                #print(rasten_array[h].commet)
                if i == 0:
                    item.setText(_translate("MainWindow", rasten_array[h].name))
                elif i == 1:
                    item.setText(_translate("MainWindow", rasten_array[h].temp))
                elif i == 2:
                    item.setText(_translate("MainWindow", rasten_array[h].time))
                elif i == 3:
                    if rasten_array[h].typ == 0:
                        item.setText(_translate("MainWindow", 'wärmer'))
                        brush = QtGui.QBrush(QtGui.QColor(255, 240, 150))
                    elif rasten_array[h].typ == 1:
                        item.setText(_translate("MainWindow", 'kälter'))
                        brush = QtGui.QBrush(QtGui.QColor(180, 180, 240))
                    elif rasten_array[h].typ == 2:
                        item.setText(_translate("MainWindow", 'egal'))
                        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
                    else:
                        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

                elif i == 6:
                    item.setText(_translate("MainWindow", rasten_array[h].comment))

                # Rührwerk und Meldung (AN/AUS)
                if i == 4:
                    boolwert = rasten_array[h].agitator
                elif i == 5:
                    boolwert = rasten_array[h].brauruf
                else:
                    boolwert = 0
                if i == 4 or i == 5:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    if boolwert:
                        brush = QtGui.QBrush(QtGui.QColor(180, 255, 180))  # grün
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        item.setBackground(brush)
                        item.setText(_translate("MainWindow", "AN"))
                    elif not boolwert:
                        brush = QtGui.QBrush(QtGui.QColor(255, 180, 180))  # rot
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        item.setBackground(brush)
                        item.setText(_translate("MainWindow", "AUS"))
                    else:
                        print('kein Boolwert')



                ui.rastenTabelle.setItem(h, i, item)



#nur zum testen
   #     for i in range(0, len(rasten_array)):
    #        print(rasten_array[i].name)



class Rast:


    def __init__(self, name: str, comment: str, temp: int, time: int, typ: int, agitator: bool, brauruf: bool):
        self.name = str(name)
        self.temp = temp
        self.time = time
        self.typ = typ
        self.agitator = agitator
        self.brauruf = brauruf
        self.comment = str(comment) #!!!evtl. .adjustSize-Methode bei Comment Item
        #               self.ID += 1 # Passt so noch nicht. Muss noch auf position angepasst werden

    # private Variablen evtl. durch Keyword @property
    # getter- / setter-Methoden
    # Sicherheit (private) (unsichere Methode __Name (für Variablen & Funktionen)
    # nur bestimmten Datentyp annehmen

    def RührwerkAn(self):
        # Ausgangsbeschaltung des Raspberrys
        pass

def changeMainWindow():

    ui.rastenTabelle.setColumnWidth(0, 300)
    ui.rastenTabelle.setColumnWidth(1, 50)
    ui.rastenTabelle.setColumnWidth(2, 60)
    ui.rastenTabelle.setColumnWidth(6, 1000)

    ui.meldungRuehrwerk.setMovie(movie)
    movie.start()

def changeDialog():
#!!!!! Größe vom Dialogfenster wieder veränderbar machen
#!!!!! Hier muss noch rein das die ComboBox nur soviele Zahlen hat wie es auch rows gibt
    dialog.positionCoB.setCurrentIndex(ui.rastenTabelle.rowCount())
#!!!!! Die aktuellen Lehrzeichen müssen entfernt werden
    dialog.temperaturLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.temperaturLE.setInputMask("00") #D damit die Zahl >0 sein muss
    dialog.dauerLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.dauerLE.setInputMask("000")

if __name__ == "__main__":

    #main
    currentID = 0
    rasten_array = []

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    movie = QtGui.QMovie("Icons\\Propeller2.gif") # nicht in Methode, weil soll noch aufgerufen werden
    movie.setScaledSize(QtCore.QSize(100, 100))

    changeMainWindow()

    ui.hinzufuegenB.clicked.connect(rastHinzufuegen)  # .connect darf nicht in "changeMainWindow()" verschoben werden
    ui.entfernenB.clicked.connect(rastEntfernen)

    NeueRastHinzufuegen = QtWidgets.QDialog()
    dialog = dialogRast.Ui_NeueRastHinzufuegen()
    dialog.setupUi(NeueRastHinzufuegen)
    changeDialog()

    #!!!!dialogRast.ui.dialogButtons.s # QDialogButtonBox mit Methode verbinden + dafür Youtubevideo ansehen
    #dialog.dialogButtons.accepted.connect(Dialog.dialogAuslesen())

    dialogC = Dialog()
    dialog.dialogButtons.accepted.connect(lambda: dialogC.dialogAuslesen())

    MainWindow.show()

    #!!!!!!! Bedingung für Exit
    sys.exit(app.exec_())