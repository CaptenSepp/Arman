import numpy as np

class SineFunction:
    """
    Diese Klasse bildet repräsentiert eine Sinusfunktion.
    Die Funktion kann ausgewertet werden (evaluate). Auch die nte Ableitung kann an der Stelle
    x0 mit evalDerivitive(n, x0) ausgewertet werden.
    Zudem ist es mögich eine textuelle Beschreibung für ein Plotlabel mit getLatex zu erhalten.
    """
    def __init__(self):
        pass

    def evalDerivitive(self, n, x):
        '''
        Berechnet den Wert der n-ten Ableitung an der Stelle (oder an den Stellen) x.
        :param n: Ordnung der Ableitung
        :param x: Skalar oder numpy-Vektor
        :return: Wert(e) als Skalar oder numpy-Vektor
        '''
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def evaluate(self, x):
        '''
        Berechnet den Wert an der Stelle (oder Stellen) x.
        :param x: Skalar oder Numpy-Vektor
        :return: Entsprechende Werte
        '''
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def getLatex(self):
        '''
        Rückgabe der Latexrepräsentation.
        :return:
        '''
        return "$sin(x)$"


#Hier nochmal der selbe Klassentyp nur mit der Exponentialfunktion
class ExpFunction:
    def __init__(self):
        pass

    def evalDerivitive(self, n, x):
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def evaluate(self, x):
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def getLatex(self):
        return "$e^x$"


class TaylorApproximation:
    def __init__(self, mathfunction, degree, x0):
        '''
        Klasse für die Repräsentation einer Taylor-Reihe
        https://de.wikipedia.org/wiki/Taylorreihe#Definition

        :param mathfunction: Zu approximierende Funktion (siehe oben. z. B. ExpFunction)
        :param degree: Grad des Taylor-Polynoms
        :param x0: Entwicklungspunkt. Dies ist die Variable "a" auf der Wikipedia-Seite
        '''
        self.fkt = mathfunction
        self.N = degree
        self.x0 = x0

    def calcTaylorCoefficients(self):
        '''
        Berechnung der Polynomkoeffizienten.
        :return: List der Koeffizienten
        Zum Beispiel steht [2, 3, 1] für das Polynom p(x) = 2 + 3x + 1x^2
        '''
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def getTaylorPolynom(self):
        '''
        Rückgabe des Polynoms vom Typ np.poly1d
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html

        :return: Polynom vom typ np.poly1d
        '''
        return [0]*4  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def evaluate(self, x):
        '''
        Auswerten der Appromximation an der Stelle (oder den Stellen) x.

        Hinweis. Verwenden Sie die Funktion getTaylorPolynom, um so ein Polynom vom typ poly1d zu
        erhalten. Ist z. B. poly ein solches Polynom, können Sie mit poly(3) der Wert für x=3 ausrechnen lassen.

        :param x: Skalar oder Vektor
        :return: Entsprechend approximierte Werte
        '''
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def getLatex(self):
        '''
        Rückgabe der Latexrepräsentation des Polynoms.
        Die Koeffizienten sollen mit drei Stellen hinter dem Dezimalpunkt ausgegeben werden.

        Beispiel: $0.551(x-x_0)^{0} + 0.834(x-x_0)^{1} - 0.276(x-x_0)^{2} - 0.139(x-x_0)^{3}$
        für ein Polynom 2. Grades an der Entwicklungsstelle x0.

        :return: String mit Latexdarstellung
        '''
        return ''  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def plotFunction(ax, x0, N, functioname):
    '''
    Plotten der approximation und der richtigen Funktion mit 400 Stellen über x = -10 ... 10.

    Es sollen 3 Plots erstellt werden.
    Genaue Funktion
    Approximation
    Marker beim Entwicklungspunkt x0

    :param ax: Achs-Objekt von Matplotlib (z. B. können Sie mit ax.plot etwas plotten)
    :param x0: Entwicklungspunkt
    :param N: Grad des Taylorpolynoms
    :param functioname: Entweder 'sin(x)' oder 'exp(x)'. Bei unbekannter Funktion wird ein ValueError geworfen.
    :return: None
    '''
    if functioname == 'sin(x)':
        fkt = SineFunction()
    elif functioname == 'exp(x)':
        fkt = ExpFunction()
    else:
        raise ValueError()
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

if __name__ == '__main__':
    import gui
    gui.run(plotFunction)
