import numpy as np


class Line:
    """
    Diese Klasse gepräsentiert das geometrische Objekt Line mit Startpunkt (p1) und Endpunkt (p2).
    """
    def __init__(self, p1xy, p2xy):
        """
        Konstruktor für das Line-Objekt.
        :param p1xy: Startpunkt als Tuple (x, y)
        :param p2xy: Endpunkt als Tuple
        """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def getEdges(self):
        """
        Gibt die beiden Punkte p1 und p2 zurück
        :return: p1,p2
        """

        return 0, 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def length(self):
        """
        Gibt die Länge der Linie zurück. (Pythagoras)

        :return: Länge der Linie
        """
        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

    def angle(self):
        """
        Winkel der Linie zur X-Achse. Stellen Sie sich vor, wie Sie
        das Steuer eine Autos drehen müssen, wenn Sie von p1 nach p2 fahren. 

                         |  p1                                          |  p2
                         |   *   phi ist ca. 300 Grad                   |   *   phi ist ca. 100 Grad
                         |    *                                         |    *
                         |     *                                        |     *
         -----------------------*------------           -----------------------*------------
                         |       *                                      |       *
                         |        *                                     |        *
                         |         *                                    |         *
                         |          p2                                  |          p1

        :return: Winkel in Grad von 0 bis 359.999999...
        """

        return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


    def rotate(self, phi):
        """
        Erzeugt ein neues Linienobjekt, dass gegenüber diesem (self) um den Grad-Winkel phi
        gedreht ist. Es wird im den Mittelpunkt der Linie gedreht.
        :param phi: Winkel in Grad 0 <= phi < 360
        :return: Line-Objekt

        Hinweise hier:https://en.wikipedia.org/wiki/Rotation_matrix
        """

        return Line((0, 0), (1, 1))  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


    def __str__(self):
        """
        Hier müssen Sie nichts machen.
        Diese Funktion dient der Anzeige Ihres Objektes mit Print
        :return: Stringrepräsentation
        """
        result = '({:5.1f}, {:5.1f}) -- ({:5.1f}, {:5.1f}) | Winkel mit X-Achse: {:5.1f}° und Länge {:5.1f}'.format(
            self.p1[0], self.p1[1], self.p2[0], self.p2[1], self.angle(), self.length()
        )
        return result


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    def plotline(ax, line, **argv):
        label = argv.get('label', '')
        label += '(Winkel = {:.1f})'.format(line.angle())
        argv['label'] = label

        p1, p2 = line.getEdges()
        p1x, p1y = p1
        p2x, p2y = p2
        ax.plot([p1x, p2x], [p1y, p2y], **argv)
        ax.plot([p1x], [p1y], marker='o', mfc='k', mec='k')

    ax = plt.gca()

    l = Line( (20, 30), (20, 10) )
    plotline(ax, l, lw=2, label='L1')
    plotline(ax, l.rotate(120), lw=2, label='L1')
    plotline(ax, l.rotate(240), lw=2, label='L1')

    l = Line( (-20, 10), (-20, 30) )
    plotline(ax, l, lw=2, label='L2')
    plotline(ax, l.rotate(120), lw=2, label='L2')
    plotline(ax, l.rotate(240), lw=2, label='L2')

    plt.xlim([-40, 40])
    plt.ylim([-40, 40])
    ax.grid()
    ax.legend()
    plt.show()
