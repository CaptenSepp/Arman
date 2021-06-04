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
        y = (n % 4)
        if   y == 0:
            return np.sin(x)
        elif y == 1:
            return np.cos(x)
        elif y == 2:
            return -np.sin(x)
        elif y == 3:
            return -np.cos(x)
        return

    def evaluate(self, x):
        '''
        Berechnet den Wert an der Stelle (oder Stellen) x.
        :param x: Skalar oder Numpy-Vektor
        :return: Entsprechende Werte
        '''
        return np.sin(x)

    def getLatex(self):
        '''
        Rückgabe der Latexrepräsentation.
        :return:
        '''
        return "$sin(x)$"


# Hier nochmal der selbe Klassentyp nur mit der Exponentialfunktion
class ExpFunction:
    def __init__(self):
        pass

    def evalDerivitive(self, n, x):
        return np.exp(x)

    def evaluate(self, x):
        return self.evalDerivitive(0, x)

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
        result = []
        for n in range(self.N+1):
            cn = self.fkt.evalDarivitive(n, self.x0) / np.math.factorial(n)
            result.append(cn)

        result.reverse()
        return result

    def getTaylorPolynom(self):
        '''
        Rückgabe des Polynoms vom Typ np.poly1d
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html

        :return: Polynom vom typ np.poly1d
        '''

        c = self.calcTaylorCoefficients()
        return np.poly1d(c)

    def evaluate(self, x):
        '''
        Auswerten der Appromximation an der Stelle (oder den Stellen) x.

        Hinweis. Verwenden Sie die Funktion getTaylorPolynom, um so ein Polynom vom typ poly1d zu
        erhalten. Ist z. B. poly ein solches Polynom, können Sie mit poly(3) der Wert für x=3 ausrechnen lassen.

        :param x: Skalar oder Vektor
        :return: Entsprechend approximierte Werte
        '''
        poly = self.getTaylorPolynom()
        return poly(x-self.x0)

    def getLatex(self):
        '''
        Rückgabe der Latexrepräsentation des Polynoms.
        Die Koeffizienten sollen mit drei Stellen hinter dem Dezimalpunkt ausgegeben werden.

        Beispiel: $0.551(x-x_0)^{0} + 0.834(x-x_0)^{1} - 0.276(x-x_0)^{2} - 0.139(x-x_0)^{3}$
        für ein Polynom 2. Grades an der Entwicklungsstelle x0.

        :return: String mit Latexdarstellung
        '''
        c = self.calcTaylorCoefficients()
        c.reverse()
        result = '$'
        for k, c in enumerate(c):
            if len(result) > 0:
                if c >= 0:
                    result += ' + '
                else:
                    c*=-1
                    result += ' - '
            result += "{:.3f}(x-x_0)^{{{:d}}}".format(c, k)
        return '${}$'.format(result)

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
    # print("Aufruf mit", x0, N, functioname)
    if functioname == 'sin(x)':
        fkt = SineFunction()
    elif functioname == 'exp(x)':
        fkt = ExpFunction()
    else:
        raise ValueError()

    taylor = TaylorApproximation(fkt, N, x0)
    x = np.linspace(-10, 10, 400)
    y = fkt.evaluate(x)
    ytaylor = taylor.evaluate(x)

    ax.plot(x, y, label=fkt.getLatex())
    ax.plot(x, ytaylor, label=taylor.getLatex())

    margin = (y.max()-y.min())*.4
    ax.set_ylim([y.min()-margin, y.min()+margin])


if __name__ == '__main__':
    import gui
    gui.run(plotFunction)
