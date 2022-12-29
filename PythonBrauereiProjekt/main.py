import datetime
import sys, time
import threading # Für .Lock()
import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, Timer
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
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

# !!! QProgressBar in QTableWidget mit .setCellWidget()
# !!! Verhindern das man Knöpfe zu häufig drücken kann (oder Arbeitsspeicherüberwachung)

class BackroundFunctions:
    @staticmethod
    def changeMainWindow():
        # !w!!! Bearbeitbarkeit der rastenTabelle entfernen
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
    @staticmethod
    def setTempPlot(value):
        set_temp_list.insert(pid.index, value)
    @staticmethod
    def curTempPlot(value):
        cur_temp_list.insert(pid.index, value)
    @staticmethod
    def heatValPlot(value):
        heat_val_list.insert(pid.index, value)

    def getValues(simulation: bool):
        if simulation is True:
            # print('getValues()')
            pid.sim_set_temp = int(set_slider.val)
            heating_value = pid.PID.run(pid.sim_set_temp, pid.sim_cur_temp)
            # print('Trägheitsliste: ' + str(pid.sim_traegheit) + '\nHeizwert: ' + str(heating_value))
            pid.sim_traegheit = pid.sim_traegheit[1:] + [float(
                heating_value)]  # !!! Hier muss noch herausgefunden werden warum kein wert zurück kommt & wie man sicherstellen kann dass einer da ist
            # print(pid.sim_traegheit)
            pid.sim_cur_temp += pid.sim_traegheit[0] / 25
            if pid.sim_cur_temp > 20:
                pid.sim_cur_temp -= pid.sim_cur_temp / 80
            # print('set: ' + str(pid.sim_set_temp) + '\ncur: ' + str(pid.sim_cur_temp) + '\nheat: ' + str(heating_value))
            print('set: ' + str(pid.sim_set_temp) + '\ncur: ' + str(pid.sim_cur_temp) + '\nheat: ' + str(heating_value))
            return pid.sim_set_temp, pid.sim_cur_temp, (heating_value * 30 + 500)
        else:
            # !!! Hier müssen die Methoden aufgerufen werden die die Werte Soll, Ist & Heat zurückgibt
            pass

    @staticmethod
    def interval():
        # Hier sollen die Wert erausgelesen und erzeugt werden
        set, cur, heat = BackroundFunctions.getValues(pid.SIM)

        pid.set_plot_y.insert(500 + pid.index, set)
        pid.cur_plot_y.insert(500 + pid.index, cur)
        pid.heat_plot_y.insert(500 + pid.index, heat)
        print('set: ' + str(pid.set_plot_y) + '\ncur: ' + str(pid.cur_plot_y) + '\nheat: ' + str(pid.heat_plot_y) + '\n')
        pid.index += 1
        return

    @staticmethod
    def plot_method():

        fig, ax1 = plt.subplots()
        fig.set_size_inches(8, 4)
        # adjust the main plot to make ROOM for the sliders
        fig.subplots_adjust(left=0.15, bottom=0.25)
        # Make a horizontal SLIDER to control the viewwidth
        viewwidth = fig.add_axes([0.15, 0.05, 0.75, 0.03])
        vw_slider = Slider(ax=viewwidth, label='Sichtweite', valmin=50, valmax=500, valinit=150)
        # Make a horizontal SLIDER to control the timepoint
        timepoint = fig.add_axes([0.15, 0.12, 0.75, 0.03])
        tp_slider = Slider(ax=timepoint, label='Zeitpunkt', valmin=0, valmax=1000,
                           valinit=1000)  # !!! 2. Slider muss noch den Zeitpunkt verändern
        # Make a vertical oriented SLIDER to control the set-temperature
        sim_soll = fig.add_axes([0.04, 0.25, 0.02, 0.58])
        set_slider = Slider(ax=sim_soll, label='Soll-Temp', valmin=0, valmax=100, valinit=80, orientation='vertical')

        ax1.set_ylabel("Temperatur in °C")  # , color="b")
        ax1.tick_params(axis="y")  # , labelcolor="b")
        line_soll, = ax1.plot(pid.set_view_y, 'k')
        line_ist, = ax1.plot(pid.cur_view_y, 'b')

        ax2 = ax1.twinx()

        ax2.set_ylabel('Heizleistung in W', color='r')
        ax2.tick_params(axis="y", labelcolor="r")
        ax2.set_ylim(200, 3800)  # für 500 - 3500 W
        line_heat, = ax2.plot(pid.heat_view_y, 'r')
        ax1.legend([line_soll, line_ist, line_heat], ['Soll-Temp', 'Ist-Temp', 'Heizleistung'])

        # print('plot-Button-Methode geht bis hier')
        ax1.grid()
        ax1.set_ylim(-10, 110)

        print('Previosshow')
        plt.show(block=False)  # block= stellt ein ob der Thread angehalten wird oder nicht
        print('Aftershow')

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
                            Rast(bezeichnung, str(kommentar), temperatur, dauer, ruehrwerk, brauruf))

        Rast.tabelleAktualisieren()


class Rast:
    """
    Klasse in der die Rasten inizialisiert werden
    """
    def __init__(self, name: str, comment: str, temp: int, duration: int, agitator: bool, signal: bool):
        self.__name = name
        self.__temp = temp
        self.__duration = duration
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



                # print(rasten_array[h].commet)
                if i == 0:
                    item.setText(_translate("MainWindow", rasten_array[h].name))
                elif i == 1:
                    item.setText(_translate("MainWindow", str(rasten_array[h].temp) + " °C"))
                elif i == 2:
                    item.setText(_translate("MainWindow", str(rasten_array[h].duration) + ' min'))
                elif i == 5:
                    item.setText(_translate("MainWindow", rasten_array[h].comment))

                # Rührwerk und Meldung (AN/AUS)
                if i == 3:
                    boolwert = rasten_array[h].agitator
                elif i == 4:
                    boolwert = rasten_array[h].signal
                else:
                    boolwert = 0
                if i == 3 or i == 4:
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

        # ProgressBar in TableWidgets
        probar = QtWidgets.QProgressBar()
        ui.rastenTabelle.setCellWidget(0,5,probar)
        probar.setValue(50)
        probar.setStyleSheet("QProgressBar::chunk {background-color: rgba(0,255,0,70)}")
        probar.setValue(75)


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

            #pidThreadI = pidThread(2, 'pid', 3, 6, 9)
            print(Clrs.cyan + 'pidThreadI erzeugt\t' + Clrs.end)

            timerThreadI.signals.progRastMax.connect(ui.progressBarRast.setMaximum)
            timerThreadI.signals.progRastVal.connect(ui.progressBarRast.setValue)
            timerThreadI.signals.progGesMax.connect(ui.progressBarGesamt.setMaximum)
            timerThreadI.signals.progGesVal.connect(ui.progressBarGesamt.setValue)
            timerThreadI.signals.timeLeft.connect(ui.sollTemp.setText)
            print('after connect')
            timerThreadI.start()
            pid.start()
            pid.interval.start()
            print(Clrs.green + 'timerThreadI gestartet\t' + Clrs.end)

            #pidThreadI.start()
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


class pidThreadSuper(QtCore.QObject):
    set_temp = QtCore.pyqtSignal(int)
    cur_temp = QtCore.pyqtSignal(float)
    heat_val = QtCore.pyqtSignal(float)


class pidThread(Thread):
    def __init__(self, threadID, name, dt, max, min, kp, ki, kd):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.PID = MyPID(0.1, 100, 0, 2.9, 0.3, 0) # dt, max, min, kp, ki, kd 2.7|0.35 | 0.01
        self.signals = pidThreadSuper()
        self.index = 0
        self.sim_cur_temp = 20
        self.sim_set_temp = int(80)
        self.sim_traegheit = list(np.zeros(5))
        self.set_view_y = list(np.full(1000, np.nan))
        self.cur_view_y = list(np.full(1000, np.nan))
        self.heat_view_y = list(np.full(1000, np.nan))
        self.set_plot_y = list(np.full(1000, np.nan))
        self.cur_plot_y = list(np.full(1000, np.nan))
        self.heat_plot_y = list(np.full(1000, np.nan))
        self.SIM = True
        # self.last_set_temp = 0
        # self.last_cur_temp = 0
        # self.last_heat_val = 0
        self.alive = True
        self.interval = QtCore.QTimer()

#Getter und Setter Methoden
    # @property
    # def alive(self):
    #     return self.alive
    #
    # @alive.setter
    # def alive(self, value: bool):
    #     self.alive = value

    def run(self) -> None:
        print(Clrs.cyan + 'pidThread beginnt\t' + Clrs.end)
        try:
            print(Clrs.cyan + "Starting: " + self.name + "\t" + Clrs.end)
            # if threadLock.locked() == False:
            #     threadLock.acquire()

            while self.alive:
                # print('set: ' + str(set) + '\ncur: ' + str(cur) + '\nheat: ' + str(heat))

                # !!! Hier müssen noch die Werte bei Änderung gespeichert werden
                # if set != pid.last_set_temp:
                #     self.signals.set_temp.emit(set)
                #     pid.last_set_temp = set
                # if cur != pid.last_cur_temp:
                #     self.signals.cur_temp.emit(cur)
                #     pid.last_cur_temp = cur
                # if heat != pid.last_heat_val:
                #     self.signals.heat_val.emit(heat)
                #     pid.last_heat_val = heat

                time_point = int(tp_slider.val * (self.index / tp_slider.valmax))

                self.set_view_y = self.set_plot_y[time_point: time_point + 1000]
                self.cur_view_y = self.cur_plot_y[time_point: time_point + 1000]
                self.heat_view_y = self.heat_plot_y[time_point: time_point + 1000]
                time.sleep(5)
                # print('set: ' + str(self.set_view_y) + '\ncur: ' + str(self.cur_view_y) + '\nheat: ' + str(self.heat_view_y))
                # !!! Hier müssen davor die arrays noch beschrieben werden
                line_soll.set_ydata(self.set_view_y)  # set_ydata
                line_ist.set_ydata(self.cur_view_y)
                line_heat.set_ydata(self.heat_view_y)

                ax1.set_xlim(500 - int(vw_slider.val), 500 + int(vw_slider.val))  # self.index+1

                fig.canvas.draw_idle()

                time.sleep(0.03)

            # if threadLock.locked():
            #     threadLock.release()
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


class MyPID:
    err = 0.0
    int = 0.0

    def __init__(self, dt, max, min, kp, ki, kd):
        self.dt = dt
        self.max = max
        self.min = min
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def run(self, set, act):
        error = set - act

        P = self.kp * error

        self.int += error * self.dt
        I = self.ki * self.int

        D = self.kd * (error - self.err) / self.dt

        output = P + I + D

        if output > self.max:
            output = self.max
        elif output < self.min:
            output = self.min

        self.err = error
        return (output)


class Clrs:
    red = "\033[31m"
    green = "\033[92m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    end = "\033[0m"

#!!! Eingangs- & Ausgangsbeschaltung
class IO:
    def __init__(self):
        pass


if __name__ == "__main__":
    currentID = 0
    rasten_array = []

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    movie = QtGui.QMovie("Icons\\Propeller2.gif")  # nicht in Methode, weil soll noch aufgerufen werden
    movie.setScaledSize(QtCore.QSize(100, 100))

    BackroundFunctions.changeMainWindow()

    # Initialisierung Kopfverbindung mit Methoden
    ui.buttonPlay.clicked.connect(lambda: ButtonFunctions.start())
    ui.buttonPause.clicked.connect(lambda: ButtonFunctions.pause())
    ui.buttonStop.clicked.connect(lambda: ButtonFunctions.stopp())
    ui.button_plot.clicked.connect(lambda: BackroundFunctions.plot_method()) # hier wird lambda benötigt
    # !!! noch in Rast Klasse verschieben
    ui.hinzufuegenB.clicked.connect(lambda: ButtonFunctions.rastHinzufuegen())  # .connect darf nicht in "changeMainWindow()" verschoben werden
    ui.entfernenB.clicked.connect(lambda: ButtonFunctions.rastEntfernen())

    pid = pidThread(2, 'pidThread', 0.1, 100, 0, 3, 0.5, 0)

    # Hier sollen die Werte später abgespeichert werden
    set_temp_list = []
    cur_temp_list = []
    heat_val_list = []

    pid.signals.set_temp.connect(BackroundFunctions.setTempPlot)
    pid.signals.cur_temp.connect(BackroundFunctions.curTempPlot)
    pid.signals.heat_val.connect(BackroundFunctions.heatValPlot)

    # Plotten in methode verschieben

    # Create the figure

    # fig, ax1 = plt.subplots()
    # fig.set_size_inches(8, 4)
    # # adjust the main plot to make ROOM for the sliders
    # fig.subplots_adjust(left=0.15, bottom=0.25)
    # # Make a horizontal SLIDER to control the viewwidth
    # viewwidth = fig.add_axes([0.15, 0.05, 0.75, 0.03])
    # vw_slider = Slider(ax=viewwidth, label='Sichtweite', valmin=50, valmax=500, valinit=150)
    # # Make a horizontal SLIDER to control the timepoint
    # timepoint = fig.add_axes([0.15, 0.12, 0.75, 0.03])
    # tp_slider = Slider(ax=timepoint, label='Zeitpunkt', valmin=0, valmax=1000,
    #                    valinit=1000)  # !!! 2. Slider muss noch den Zeitpunkt verändern
    # # Make a vertical oriented SLIDER to control the set-temperature
    # sim_soll = fig.add_axes([0.04, 0.25, 0.02, 0.58])
    # set_slider = Slider(ax=sim_soll, label='Soll-Temp', valmin=0, valmax=100, valinit=80, orientation='vertical')

    # line_soll, = ax1.plot(list(np.full(1000, np.nan)), 'k')
    # line_ist, = ax1.plot(list(np.full(1000, np.nan)), 'b')
    # ax2 = ax1.twinx()
    # line_heat, = ax2.plot(list(np.full(1000, np.nan)), 'r')

    # BackroundFunctions.plot_method()
    # pid.start()
    # pid.interval.start()
    pid.interval.timeout.connect(lambda: BackroundFunctions.interval())
    pid.interval.setInterval(500)  # 3000ms

    # muss mit Plot von main-Thread in Button-Func ausgeführt werden

    # Initialisierung Timer
    timer = MyTimer()
    threadLock = threading.Lock()

    NeueRastHinzufuegen = QtWidgets.QDialog()
    dialog = dialogRast.Ui_NeueRastHinzufuegen() # Klasse von dialogRast.py
    dialog.setupUi(NeueRastHinzufuegen)
    BackroundFunctions.changeDialog()

    dialogC = Dialog()
    dialog.dialogButtons.accepted.connect(lambda: dialogC.dialogAuslesen())

    MainWindow.show()

    # !!!!!!! Bedingung für Exit // funktioniert noch nicht
    app.exec_()
    print('bye')


    timerThread.alive = False
    pid.alive = False
    sys.exit(0)
