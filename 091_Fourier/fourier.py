import numpy as np
import sympy as sp
from sympy.core.sympify import SympifyError
import pandas as pd

class Creator:
    def __init__(self):
        pass

    def evaluate(self):
        '''
        Die Funktion erstellt einen Zeit und Funktionsvektor.
        Entsprechend dem auf der Benutzerfläche angegebenen Ausdruck.

        Bitte schauen Sie sich für die Auswertung von beliebigen Ausdrücken
        * https://docs.sympy.org/latest/modules/utilities/lambdify.html
        * sympy wird oben als sp importiert
        * Sie können einen beliebigen Ausdruckt (expr) mit der Variable 'x' z. B. mit
          f = sp.lambdify('x', expr)  # Erstellt eine Funktion, die den Ausdruck auswertet
          y = f(1) #Wertet den Ausdruck für x=1 aus.
          y = f( np.array([1, 2, 3]) ) #Es können auch Numpy-Arrays übergeben werden.


        :return:
            (t, y)
            t sind die Zeitpunkte der Abtastung (von 0s - Dauer) Allerdings ohne den letzten Punkt.
            Wenn es also z. B. 10 Abtastzeitpunkte und eine Dauer von 1 Sekunde gegeben sind, dann ist
            t = [0, 0.1, 0.2, ..., 0.9]
            y sind dann die enstprechenden Funktionswerte f(t)
        '''
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def writeToExcel(self, t, y):
        '''
        Schreibt eine Exceldatei mit dem Dateinamen der "Ausgabedatei"
        Die Spalten der Excel-Datei sind "t" und "y".
        Schauen Sie sich dafür die Funktion to_excel der DataFrame-Klasse aus Pandas an.

        :param t: Zeitvektor
        :param y: Funktionsvector
        :return: None
        '''
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def set(self, Abtastfrequenz, Dauer, Ausgabedatei, Ausdruck):
        '''
        Hier werden die  Parameter durch die GUI gesetzt.
        :param Abtastfrequenz: Achtung wird als str übergeben
        :param Dauer: Achtung wird als str übergeben
        :param Ausgabedatei: str
        :param Ausdruck: str (Mathematischer Ausdruck wie z. b. sin(2*pi*t*10)
        :return:
        '''
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def do(self):
        '''
        Ausführung. Hier müssen Sie nichts mehr ändern
        :return:
        '''
        t, y = self.evaluate()
        self.writeToExcel(t, y)



class Analyzer:
    def __init__(self):
        pass

    def set(self, Eingabedatei, ax1, ax2):
        '''
        Setzen der Parameter durch die Gui
        :param Eingabedatei: Dateiname der Excel-Datei
        :param ax1: Axis-Objekt, mit dem geplottet werden kann
        :param ax2: Axis-Objekt, mit dem geplottet werden kann
        :return:
        '''
        self.filename = Eingabedatei
        self.ax1 = ax1
        self.ax2 = ax2

    def readData(self):
        '''
        Liest die Daten aus der Excel-Datei (Eingabedatei) aus.
        :return:
        t, y
        '''
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def calcFourierCoefficients(self, t, y):
        '''
        Berechnung der Fourier-Koeffizienten.

        Dabei berechnen sich der Koeffizient c_k zugehörig zu einer Frequenz f_k mit
                            T
        c_k = 2/T * integal | x(t) * exp(-j2pi f_k t) dt
                            0

        Wir können hier natürlich keine Integrale lösen und nähern uns mit einer Summe an:

        c_k = 2/T * sum[k=0, k=N-1] x_k * exp(-j2pi f_k t_k) * dt

        Wobei N = Hälfte der Abtastwerte + 1
              dt = Abstand zweier Zeitwerte (z. B. t[1]-t[0])
              f_k = k/(2*dt*(N-1))

        Beispiel: Bei t = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
                  Ist
                  N = 4
                  dt = 0.2
                  T = 1.2
                  f = [0.0, 0.833, 1.67, 2.5]
        :param t: Zeitvektor
        :param y: Abtastwerte (Funktionswerte)
        :return: (f, c)
        f: Vektor mit f_k
        c: Vector mit c_k
        '''
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    #Ab hier müssen Sie nichts mehr ändern

    def plotTimeSignal(self, t, y):
        ax = self.ax1

        ax.plot(t*1e3, y)
        ax.set_title('Zeitbereichsdarstellung')
        ax.set_xlabel('t [ms]')
        ax.set_ylabel('Amplitude')
        ax.grid()

    def plotAmplitudeSpectrum(self, f, c):
        ax = self.ax2

        ax.plot(f, abs(c), marker='.', color='k')
        ax.set_title('Fourier Koeffizienten')
        ax.set_xlabel('f [Hz]')
        ax.set_ylabel('Amplitude')
        ax.grid()

        from matplotlib.ticker import ScalarFormatter
        for axis in [ax.xaxis]:
            axis.set_major_formatter(ScalarFormatter())


    def do(self):
        t, y = self.readData()
        f, c = self.calcFourierCoefficients(t, y)
        self.plotTimeSignal(t, y)
        self.plotAmplitudeSpectrum(f, c)

if __name__ == '__main__':
    import gui
    gui.run(Creator(), Analyzer())

