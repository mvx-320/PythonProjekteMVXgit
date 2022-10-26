import datetime
import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, Timer
from datetime import datetime, timedelta

import main  # Braucht man für currentID
import ui1, dialogRast


# Github Upload:
# neues Commit erstellen auf Git->Commit...
# Push (oben rechts) von ThisIsMyBranch -> origin, master

# FEHLERBEHEBUNG:
# thread handling + sync/lock (volatile gibt es nicht)

# !!! Editierbarkeit bei allen Items wie bei Item 0,0
# !!! Typ entfernen start nach Temperaturannäherung in Einstellungen bearbeitbar
# !!! QProgressBar in QTableWidget mit .setCellWidget()
# !!! Verhindern das man Knöpfe zu häufig drücken kann (oder Arbeitsspeicherüberwachung)

# Rast Hinzufügen Button gedrückt
def rastHinzufuegen():
    main.currentID = ui.rastenTabelle.rowCount() + 1
    dialog.positionCoB.clear()
    for i in range(main.currentID):
        dialog.positionCoB.addItem(str(i + 1))
    dialog.positionCoB.setCurrentIndex(main.currentID - 1)
    dialog.bezeichnungLE.clear()
    dialog.temperaturLE.clear()
    dialog.dauerLE.clear()
    dialog.typCoB.setCurrentIndex(0)
    dialog.ruehrwerkChB.setCheckState(0)
    dialog.braurufChB.setCheckState(0)
    dialog.kommentarTE.clear()

    NeueRastHinzufuegen.show()

    # !!!!!!! Abchecken ob man neues VericalItem erzeugen muss // Bisher nicht


# Rast Enfernen Button gedrückt
def rastEntfernen():
    # timer.resume()
    if len(rasten_array) > 0:
        loeschAnfrage = QtWidgets.QMessageBox()
        loeschAnfrage.setWindowTitle('Rast löschen?')
        loeschAnfrage.setText('Soll die Rast wirklich gelöscht werden?')
        pixmap = QtGui.QPixmap("Icons/müll3.png")

        loeschAnfrage.setIconPixmap(pixmap)
        loeschAnfrage.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # loeschAnfrage.setInformativeText('(Rast wird dauerhaft gelöscht)')
        loeschAnfrage.accepted.connect(Rast.rastLoeschen)
        msg = loeschAnfrage.exec_()


class Dialog:
    @staticmethod
    def dialogAuslesen():
        #!!! Abfragen ob die Felder befüllt sind
        if dialog.dauerLE.text() == '':
            NeueRastHinzufuegen.show()
            return
        main.currentID = dialog.positionCoB.currentIndex() + 1
        bezeichnung = dialog.bezeichnungLE.text()
        temperatur = dialog.temperaturLE.text()
        dauer = dialog.dauerLE.text()
        typ = dialog.typCoB.currentIndex()
        if dialog.ruehrwerkChB.checkState() == 2:  # 0 = Unchecked; 2 = Checked
            ruehrwerk = True
        else:
            ruehrwerk = False
        if dialog.braurufChB.checkState() == 2:
            brauruf = True
        else:
            brauruf = False
        kommentar = dialog.kommentarTE.document().toPlainText()
        kommentar = kommentar.replace('\n', '  ')

        if main.currentID > len(rasten_array) + 1:
            main.currentID = len(rasten_array) + 1
        if main.currentID < 1:
            main.currentID = 1

        rasten_array.insert(main.currentID - 1,
                            Rast(bezeichnung, str(kommentar), temperatur, dauer, typ, ruehrwerk, brauruf))

        Rast.tabelleAktualisieren()


class Rast:
    def __init__(self, name: str, comment: str, temp: int, time: int, typ: int, agitator: bool, brauruf: bool):
        self.name = str(name)
        self.temp = temp
        self.time = time  # Hier stimmt was nicht

        self.typ = typ
        self.agitator = agitator
        self.brauruf = brauruf
        self.comment = str(comment)  # !!!evtl. .adjustSize-Methode bei Comment Item

    @staticmethod
    def tabelleAktualisieren():
        _translate = QtCore.QCoreApplication.translate
        ui.rastenTabelle.setRowCount(len(rasten_array))
        for i in range(len(rasten_array)):
            ui.rastenTabelle.setRowHeight(i, 50)

        for h in range(0, len(rasten_array)):
            # print(h)
            for i in range(ui.rastenTabelle.columnCount()):
                item = QtWidgets.QTableWidgetItem()

                # Blaufärbung bei jeder 2. Zeile
                if h % 2 == 0:
                    brush = QtGui.QBrush(QtGui.QColor(240, 240, 255))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

                # print(rasten_array[h].commet)
                if i == 0:
                    item.setText(_translate("MainWindow", rasten_array[h].name))
                elif i == 1:
                    item.setText(_translate("MainWindow", str(rasten_array[h].temp) + " °C"))
                elif i == 2:
                    item.setText(_translate("MainWindow", str(rasten_array[h].time) + ' min'))
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
                        print('FEHLER: kein Boolwert')

                ui.rastenTabelle.setItem(h, i, item)

    @staticmethod
    def rastLoeschen():
        r = ui.rastenTabelle.currentRow()
        rasten_array.remove(rasten_array[r])
        Rast.tabelleAktualisieren()

    # private Variablen evtl. durch Keyword @property
    # getter- / setter-Methoden
    # Sicherheit (private) (unsichere Methode __Name (für Variablen & Funktionen)
    # nur bestimmten Datentyp annehmen

    def RührwerkAn(self):
        # Ausgangsbeschaltung des Raspberrys
        pass


class Runtime:
    @staticmethod
    def start():
        # !!!hier Visualisierung in den Runmodus setzen

        #threads = []
        timerThreadI = timerThread(1, 'timer', 12)
       #pidThreadI = pidThread(2, 'pid', 1, 2, 3)

        timerThreadI.start()
        #pidThreadI.start()
        ########Threads in threads-Array und starten
        #threadTime = Thread(target=Runtime.timerRun, name="zeit", args=['abschalten'])
        #threadPID = Thread(target=Runtime.pidRegelung, name="pid", args=['pidRegler'])
        #print("Threads werden erzeugt")
        #threads.append(threadTime)
        #threadTime.start()
        ##Hier dazwischen darf nichts stehen???
        #threads.append(threadPID)
        #threadPID.start()

    @staticmethod
    def pause():
        #timer.pause()
        pass

    @staticmethod
    def stopp():
        pass

    #808 hier war timerRun()


    @staticmethod  # Thread
    def pidRegelung(name):
        print(name + '-Thread start')

    @staticmethod
    def time_to_num(time_str):
        hh, mm, ss = map(int, time_str.split(':'))
        return ss + 60 * (mm + 60 * hh)

class MyThread(Thread):
    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name

class timerThread(MyThread):
    def __init__(self, threadID: int, name: str, time: float):
        MyThread.__init__(self, threadID, name)
        self.time = time

    def run(self) -> None:
        print("Starting: " + self.name + "\n")
        if threadLock.locked():
            threadLock.release()
        threadLock.acquire()

        if timer.timestarted != None:
            timer.resume()
        else:
            timer.start()

        ges_zeit = 0
        for rasten in rasten_array:
            ges_zeit += int(rasten.time)
        #gesamtZeit = timedelta(minutes=float(ges_zeit))
        #aktuelleZeit = timedelta(minutes=float(rasten_array[0].time))
        while True:#timer.get() < aktuelleZeit
            timeSEC = timer.get()
            #print(timeSEC)
            timeNOW = [int(timeSEC/60)%3600, int(timeSEC)%10, int(timeSEC*10)%10]
            ui.sollTemp.setText(str(f'Time: {timeNOW[0]}:{timeNOW[1]}.{timeNOW[2]}'))


        timer.timestarted = None

        threadLock.release()
        print("Exiting: " + self.name + "\n")

class pidThread(MyThread):
    def __int__(self, threadID: int, name: str, pValue: float, iValue: float, dValue: float):
        MyThread.__init__(self, threadID, name)
        self.pValue = pValue
        self.iValue = iValue
        self.dValue = dValue

    def run(self) -> None:
        print("Starting: " + self.name + "\n")
        if threadLock.locked():
            threadLock.release()
        threadLock.acquire()
        pass
        threadLock.release()
        print("Exiting: " + self.name + "\n")

# Hier ist noch kein Objekt instanziiert
class MyTimer():
    """
    timer.start() - should start the timer
    timer.pause() - should pause the timer
    timer.resume() - should resume the timer
    timer.get() - should return the current time
    """

    def __init__(self):
        # print('Initializing timer')
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def start(self):
        #""" Starts an internal timer by recording the current time """
        print("Starting timer")
        self.timestarted = time.time()

    def pause(self):
        #""" Pauses the timer """
        if self.timestarted is None:
            print("Timer not started")
            #raise ValueError("Timer not started")
        if self.paused:
            print("Timer is already paused")
            #raise ValueError("Timer is already paused")
        print('Pausing timer')
        self.timepaused = time.time()
        self.paused = True


    def resume(self):
        #""" Resumes the timer by adding the pause time to the start time """
        if self.timestarted is None:
            print("Timer not started")
            #raise ValueError("Timer not started")
        if not self.paused:
            print("Timer is not paused")
            #raise ValueError("Timer is not paused")
        print('Resuming timer')
        pausetime = time.time() - self.timepaused
        self.timestarted = self.timestarted + pausetime
        self.paused = False

    def get(self):
        """ Returns a timedelta object showing the amount of time
            elapsed since the start time, less any pauses """
        # print('Get timer value')
        if self.timestarted is None:
            print("Timer not started")
            #raise ValueError("Timer not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return time.time() - self.timestarted

def changeMainWindow():
    # !w!!! Bearbeitbarkeit der rastenTabelle entwernen
    # !w!!! rastenTabelle bearbeiten mit auswählen und dann vorausgewähltem Feld im Dialogfenster
    ui.rastenTabelle.setColumnWidth(0, 300)
    ui.rastenTabelle.setColumnWidth(1, 100)
    ui.rastenTabelle.setColumnWidth(2, 120)
    ui.rastenTabelle.setColumnWidth(6, 1000)
    ui.progressBarRast.setFixedHeight(10)
    ui.progressBarGesamt.setFixedHeight(20)

    ui.meldungRuehrwerk.setMovie(movie)
    movie.start()


def changeDialog():
    # !!!!! Größe vom Dialogfenster wieder veränderbar machen // evtl noch kleiner
    dialog.positionCoB.setCurrentIndex(ui.rastenTabelle.rowCount())
    # !!!!! Die aktuellen Lehrzeichen müssen entfernt werden // evtl schon draußen
    dialog.temperaturLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.temperaturLE.setInputMask("00")  # D damit die Zahl >0 sein muss
    dialog.dauerLE.setAlignment(QtCore.Qt.AlignCenter)
    dialog.dauerLE.setInputMask("000")


def programmVerlassen():
    print('Beim Schließen nachfragen')
    return app.exec_()


if __name__ == "__main__":
    currentID = 0
    rasten_array = []

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    movie = QtGui.QMovie("Icons\\Propeller2.gif")  # nicht in Methode, weil soll noch aufgerufen werden
    movie.setScaledSize(QtCore.QSize(100, 100))

    changeMainWindow()

    # Initialisierung Kopfverbindung mit Methoden
    ui.buttonPlay.clicked.connect(Runtime.start)
    ui.buttonPause.clicked.connect(Runtime.pause)
    ui.buttonStop.clicked.connect(Runtime.stopp)
    # !!! noch in Rast Klasse verschieben
    ui.hinzufuegenB.clicked.connect(rastHinzufuegen)  # .connect darf nicht in "changeMainWindow()" verschoben werden
    ui.entfernenB.clicked.connect(rastEntfernen)

    # Initialisierung Timer
    timer = MyTimer()
    threadLock = threading.Lock()

    NeueRastHinzufuegen = QtWidgets.QDialog()
    dialog = dialogRast.Ui_NeueRastHinzufuegen() # Klasse von dialogRast.py
    dialog.setupUi(NeueRastHinzufuegen)
    changeDialog()

    dialogC = Dialog()
    dialog.dialogButtons.accepted.connect(lambda: dialogC.dialogAuslesen())

    MainWindow.show()

    # !!!!!!! Bedingung für Exit // funktioniert noch nicht
    sys.exit(app.exec_())
