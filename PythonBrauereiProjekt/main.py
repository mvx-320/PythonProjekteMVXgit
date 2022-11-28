import datetime
import sys
import threading
import time
import traceback
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
# FRAGE:
# Warum friert bild nach 15min ein || Schreibfehler __init__() warum keine Exception my pyCharm und bei der CMD schon

# !!! Editierbarkeit bei allen Items wie bei Item 0,0
# !!! Typ entfernen start nach Temperaturannäherung in Einstellungen bearbeitbar
# !!! QProgressBar in QTableWidget mit .setCellWidget()
# !!! Verhindern das man Knöpfe zu häufig drücken kann (oder Arbeitsspeicherüberwachung)

class BackroundFunktions:
    @staticmethod
    def changeMainWindow():
        # !w!!! Bearbeitbarkeit der rastenTabelle entwernen
        # !w!!! rastenTabelle bearbeiten mit auswählen und dann vorausgewähltem Feld im Dialogfenster
        ui.rastenTabelle.setColumnWidth(0, 300)
        ui.rastenTabelle.setColumnWidth(1, 100)
        ui.rastenTabelle.setColumnWidth(2, 120)
        ui.rastenTabelle.setColumnWidth(6, 1000)
        # !!!Value in QtCreator gesetzt
        ui.progressBarRast.setValue(0)
        ui.progressBarGesamt.setValue(0)
        # !!!Höhe in QtCreator setzen
        ui.progressBarRast.setFixedHeight(10)
        ui.progressBarGesamt.setFixedHeight(20)

        ui.meldungRuehrwerk.setMovie(movie)
        movie.start()

    @staticmethod
    def changeDialog():
        # !!!!! Größe vom Dialogfenster wieder veränderbar machen // evtl noch kleiner
        dialog.positionCoB.setCurrentIndex(ui.rastenTabelle.rowCount())
        # !!!!! Die aktuellen Lehrzeichen müssen entfernt werden // evtl schon draußen
        dialog.temperaturLE.setAlignment(QtCore.Qt.AlignCenter)
        dialog.temperaturLE.setInputMask("00")  # D damit die Zahl >0 sein muss
        dialog.dauerLE.setAlignment(QtCore.Qt.AlignCenter)
        dialog.dauerLE.setInputMask("000")

    @staticmethod
    def programmVerlassen():
        print('Beim Schließen nachfragen')
        return app.exec_()


class Dialog:
    @staticmethod
    def dialogAnzeigen():
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

    @staticmethod
    def dialogAuslesen():
        #!!! Abfragen ob die Felder befüllt sind
        if dialog.dauerLE.text() == '':
            NeueRastHinzufuegen.show()
            return
        #!!! temp muss auch ausgefüllt sein
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
        kommentar = kommentar.replace('\n', '\t')

        if main.currentID > len(rasten_array) + 1:
            main.currentID = len(rasten_array) + 1
        if main.currentID < 1:
            main.currentID = 1

        rasten_array.insert(main.currentID - 1,
                            Rast(bezeichnung, str(kommentar), temperatur, dauer, typ, ruehrwerk, brauruf))

        Rast.tabelleAktualisieren()


class Rast:
    """
    Klasse in der die Rasten inizialisiert werden
    """
    def __init__(self, name: str, comment: str, temp: int, duration: int, typ: int, agitator: bool, signal: bool):
        self.__name = name
        self.__temp = temp
        self.__duration = duration
        self.__typ = typ
        self.__agitator = agitator
        self.__signal = signal
        self.__comment = comment  # !!!evtl. .adjustSize-Methode bei Comment Item

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, value: str):
        self.__temp = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value: str):
        self.__duration = value

    @property
    def typ(self):
        return self.__typ

    @typ.setter
    def typ(self, value: str):
        self.__typ = value

    @property
    def agitator(self):
        return self.__agitator

    @agitator.setter
    def agitator(self, value: str):
        self.__agitator = value

    @property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, value: str):
        self.__signal = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value: str):
        self.__comment = value

    @staticmethod
    def tabelleAktualisieren():
        """
        Aktuallisiert die Tabelle, in der die Rasten abgebildet werden.
        Die Tabelle wird mit dem Array synchronisiert.
        """
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
                    item.setText(_translate("MainWindow", str(rasten_array[h].duration) + ' min'))
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
                    boolwert = rasten_array[h].signal
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

    def RuehrwerkAn(self):
        # Ausgangsbeschaltung des Raspberrys
        pass


class ButtonFunctions:
    # Rast Hinzufügen Button gedrückt
    @staticmethod
    def rastHinzufuegen():
        Dialog.dialogAnzeigen()

    # Rast Enfernen Button gedrückt
    @staticmethod
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
            loeschAnfrage.exec_()

    @staticmethod
    def start(): # Button Start
        # !!!hier Visualisierung in den Runmodus setzen

        try:
            timerThread.alive = True
            # ButtonFunctions.threadInit(i)
            timerThreadI = timerThread(1, 'timer')
            print(Clrs.green + 'timerThreadI erzeugt\t' + Clrs.end)

            pidThreadI = pidThread(2, 'pid', 3, 6, 9)
            print(Clrs.cyan + 'pidThreadI erzeugt\t' + Clrs.end)

            timerThreadI.signals.progRastMax.connect(ui.progressBarRast.setMaximum)
            timerThreadI.signals.progRastVal.connect(ui.progressBarRast.setValue)
            timerThreadI.signals.progGesMax.connect(ui.progressBarGesamt.setMaximum)
            timerThreadI.signals.progGesVal.connect(ui.progressBarGesamt.setValue)
            timerThreadI.signals.timeLeft.connect(ui.sollTemp.setText)

            timerThreadI.start()
            print(Clrs.green + 'timerThreadI gestartet\t' + Clrs.end)

            pidThreadI.start()
            print(Clrs.cyan + 'pidThreadI gestartet\t' + Clrs.end)

        except Exception:
            print(Clrs.red + traceback.format_exc() + Clrs.end)

        except:
            print(Clrs.red + traceback.format_exc() + Clrs.end)
        else:
            print(Clrs.green + 'done: Runtime' + '\t' + Clrs.end)



    @staticmethod
    def threadInit(step: int):
        if step == 0:
           pass
        elif step == 1:
           pass
    @staticmethod # Button Pause
    def pause():
        #ui.rastenTabelle.setSelection(QtCore.QRect(QtCore.QPoint(0, 1), QtCore.QSize(1, 2))
        timer.pause()
        return


    @staticmethod # Button Stopp
    def stopp():
        # Funktioniert nicht
        timerThread.alive = False
        timer.pause()
        timer.timestarted = None
        timer.timepaused = None
        timer.paused = False
        pass

    #808 hier war timerRun()


class timerThreadSuper(QtCore.QObject):
    progRastMax = QtCore.pyqtSignal(int)
    progRastVal = QtCore.pyqtSignal(int)
    progGesMax = QtCore.pyqtSignal(int)
    progGesVal = QtCore.pyqtSignal(int)
    timeLeft = QtCore.pyqtSignal(str)


class timerThread(Thread):
    """
    Klasse des timer Threads
    """

    def __init__(self, threadID: int, name: str):
        """
        Hier wird das timer Thread Objekt initialisiert
        """
        super(timerThread, self).__init__(), super(timerThread, self).__init__()
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.__alive = True
        self.signals = timerThreadSuper()

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value: bool):
        self.__alive = value

    @QtCore.pyqtSlot()
    def run(self) -> None:
        print(Clrs.green + 'timerThread beginnt \t' + Clrs.end)
        try:
            print(Clrs. green + "Starting: " + self.name + "\t" + Clrs.end)
            if threadLock.locked() == False:
                threadLock.acquire()

            if timer.timestarted != None:
                timer.resume()
            else:
                timer.start()

            ges_zeit_min = 0
            for rasten in rasten_array:
                ges_zeit_min += int(rasten.duration)
            ges_zeit_sec = ges_zeit_min * 60
            #SafetyFunctions.QProgressbarSetMaximum(ui.progressBarGesamt, ges_zeit_sec)
            self.signals.progGesMax.emit(ges_zeit_sec * 60)

            end_rast_time_sec = 0
            for timeIndex in range(len(rasten_array)):
                try:
                    current_rast_time_min = (int(rasten_array[timeIndex].duration))
                    end_rast_time_sec += current_rast_time_min * 60
                    past_rast_time_sec = end_rast_time_sec - current_rast_time_min * 60
                    self.signals.progRastMax.emit(current_rast_time_min * 60 * 60)
                except:
                    print(Clrs.red + traceback.format_exc() + Clrs.end)
                    break
                while self.alive:
                    timer_sec = timer.get()
                    timer_sec_list = [int(timer_sec / 60) % 3600, int(timer_sec) % 60, int(timer_sec * 10) % 10]
                    value_rast_prog = timer_sec - past_rast_time_sec
                    self.signals.progGesVal.emit(int(timer_sec * 60))
                    self.signals.progRastVal.emit(int(value_rast_prog * 60))
                    self.signals.timeLeft.emit(str(f'Time: {timer_sec_list[0]}:{timer_sec_list[1]}.{timer_sec_list[2]}'))
                    if timer_sec > float(end_rast_time_sec):
                        print(Clrs.blue + 'Timer abgelaufen' + Clrs.end)
                        break

                    #!!!Fehlermeldungen:
                    # QObject::setParent: Cannot set parent, new parent is in a different thread
                    # QWidget::repaint: Recursive repaint detected
                    # QBackingStore::endPaint() called with active painter; did you forget to destroy it or call QPainter::end() on it?
                    # Fehlerbehebung: -auf stackoverflow beschrieben. Link in PythonProjekt Ordner Firefox
                    # Die Q-Klassen dürfen nur vom MainThread beschrieben werden
                    # -> run-Funktionen der Threads überabeiten. Außerdem außerhalb der Methoden nach Aufrufen sehen
                    # -> SafetyFunctions QProgressBarSetMaximum muss ebenfalls überarbeitet werden



            timer.timestarted = None
            if threadLock.locked():
                threadLock.release()
            print(Clrs.green + "Exiting: " + self.name + "\t" + Clrs.end)
        except Exception:
            print(Clrs.red + traceback.format_exc() + Clrs.end)
        except:
            print(Clrs.red + traceback.format_exc() + Clrs.end)
        else:
            print(Clrs.green + 'done: timerThread' + Clrs.end)


class pidThread(Thread):
    def __init__(self, threadID: int, name: str, pValue: float, iValue: float, dValue: float):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.pValue = pValue
        self.iValue = iValue
        self.dValue = dValue
        self.__alive = True

    @property
    def alive(self):
        return self.alive

    @alive.setter
    def alive(self, value: bool):
        self.alive = value

    def run(self) -> None:
        print(Clrs.cyan + 'pidThread beginnt\t' + Clrs.end)
        try:
            print(Clrs.cyan + "Starting: " + self.name + "\t" + Clrs.end)
            if threadLock.locked() == False:
                threadLock.acquire()
            pass
            if threadLock.locked():
                threadLock.release()
            print(Clrs.cyan + "Exiting: " + self.name + "\t" + Clrs.cyan)
        except Exception:
            print(Clrs.red + traceback.format_exc() + Clrs.end)
        except:
            print(Clrs.red + traceback.format_exc() + Clrs.end)
        else:
            print(Clrs.cyan + 'done: pidThread' + Clrs.end)

# Hier ist noch kein Objekt instanziiert
class MyTimer():
    """
    timer.start() - should start the timer
    timer.pause() - should pause the timer
    timer.resume() - should resume the timer
    timer.get() - should return the current time
    """

    def __init__(self):
        print(Clrs.magenta + 'Initializing timer' + Clrs.end)
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def start(self):
        """ Starts an internal timer by recording the current time """
        print(Clrs.magenta + "Starting MyTimer\t" + Clrs.end)
        self.timestarted = time.time()

    def pause(self):
        """ Pauses the timer """
        if self.timestarted is None:
            print(Clrs.red + "Timer not started" + Clrs.end)
            #raise ValueError("Timer not started")
        if self.paused:
            print(Clrs.red + "Timer is already paused" + Clrs.end)
            #raise ValueError("Timer is already paused")
        print(Clrs.magenta + 'Pausing timer' + Clrs.end)
        self.timepaused = time.time()
        self.paused = True

    def resume(self):
        """ Resumes the timer by adding the pause time to the start time """
        if self.timestarted is None:
            print(Clrs.red + "Timer not started" + Clrs.end)
            # raise ValueError("Timer not started")
        if not self.paused:
            print(Clrs.red + "Timer is not paused" + Clrs.end)
            # raise ValueError("Timer is not paused")
        print(Clrs.magenta + 'Resuming timer' + Clrs.end)
        pausetime = time.time() - self.timepaused
        self.timestarted = self.timestarted + pausetime
        self.paused = False

    def get(self):
        """ Returns a timedelta object showing the amount of time
            elapsed since the start time, less any pauses """
        #print(Clrs.magenta + 'Get timer value' + Clrs.end)
        if self.timestarted is None:
            print(Clrs.red + "Timer not started" + Clrs.end)
            #raise ValueError("Timer not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return time.time() - self.timestarted


class Clrs:
    red = "\033[31m"
    green = "\033[92m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    end = "\033[0m"


if __name__ == "__main__":
    currentID = 0
    rasten_array = []

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    movie = QtGui.QMovie("Icons\\Propeller2.gif")  # nicht in Methode, weil soll noch aufgerufen werden
    movie.setScaledSize(QtCore.QSize(100, 100))

    BackroundFunktions.changeMainWindow()

    # Initialisierung Kopfverbindung mit Methoden
    ui.buttonPlay.clicked.connect(lambda: ButtonFunctions.start())
    ui.buttonPause.clicked.connect(lambda: ButtonFunctions.pause())
    ui.buttonStop.clicked.connect(lambda: ButtonFunctions.stopp())
    # !!! noch in Rast Klasse verschieben
    ui.hinzufuegenB.clicked.connect(lambda: ButtonFunctions.rastHinzufuegen())  # .connect darf nicht in "changeMainWindow()" verschoben werden
    ui.entfernenB.clicked.connect(lambda: ButtonFunctions.rastEntfernen())




    # Initialisierung Timer
    timer = MyTimer()
    threadLock = threading.Lock()

    NeueRastHinzufuegen = QtWidgets.QDialog()
    dialog = dialogRast.Ui_NeueRastHinzufuegen() # Klasse von dialogRast.py
    dialog.setupUi(NeueRastHinzufuegen)
    BackroundFunktions.changeDialog()

    dialogC = Dialog()
    dialog.dialogButtons.accepted.connect(lambda: dialogC.dialogAuslesen())

    MainWindow.show()

    # !!!!!!! Bedingung für Exit // funktioniert noch nicht
    app.exec_()
    print('bye')


    timerThread.alive = False
    pidThread.alive = False
    sys.exit(-1)
