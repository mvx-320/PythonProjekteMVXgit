#!/usr/bin/python3
# ------------------------------------------------------------------------------
# Python 3.4.3
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# includes
# ------------------------------------------------------------------------------
import os
import sys
from matplotlib import pyplot as plt
import time
from threading import Thread

# ------------------------------------------------------------------------------
import main
# Fallnummer JBL: 11092708

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

        #self.set_temp = None

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

# --------------------------------------------------------------------------------

class graphThread(Thread):
    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self) -> None:
        print('Thread start')
        val = 20
        traegheit = [0 for i in range(2)]
        for i in range(100):
            valGraph.insert(i, val)
            inc = pid.run(80, val)  # sollwert, istwert
            incGraph.insert(i, inc)
            print('val:', '{:7.3f}'.format(val), ' inc:', '{:7.3f}'.format(inc))

            # Für Simulation (in echt muss val ausgelesen & berechnet werden und inc geschrieben)
            traegheit = [inc] + traegheit[1:]
            val += traegheit[0]/25
            val -= val / 80

            # Anzeige plot
            plt.cla()
            plt.ylim([-20,120])
            plt.xlim([i-10,i+10])
            plt.grid()
            plt.plot((0,0), (-10,110), color ='black') # Startline
            plt.plot(valGraph, 'b')
            plt.plot(incGraph, 'r')
            plt.draw()
            time.sleep(0.1)

# ------------------------------------------------------------------------------
def close():
    print('close')
if __name__ == '__main__':
    valGraph, incGraph = [], []  # list(range(100))
    plt.plot(valGraph)
    pid = MyPID(0.1, 100, 0, 2.9, 0.3, 0) # dt, max, min, kp, ki, kd 2.7|0.35 | 0.01
    thread = graphThread(3, 'graphThread')
    thread.start()
    plt.show()
    plt.close(close())
# --------------------------------------------------------------------------