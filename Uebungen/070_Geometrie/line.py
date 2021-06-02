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
        self.p1 = np.array(p1xy)
        self.p2 = np.array(p2xy)

    def getEdges(self):
        """
        Gibt die beiden Punkte p1 und p2 zurück
        :return: p1,p2
        """

        return self.p1, self.p2

    def length(self):
        """
        Gibt die Länge der Linie zurück. (Pythagoras)

        :return: Länge der Linie
        """

        ak = self.p2[0] - self.p1[0]
        gk = self.p2[1] - self.p1[1]
        length = np.sqrt(ak ** 2 + gk ** 2)

        return length

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

        # delta = self.p2 - self.p1
        # dx, dy = delta
        # angle = np.arctan2(dy, dx) * 180 / np.pi
        # angle = (angle + 360) % 360

        p1x, p1y = self.p1
        p2x, p2y = self.p2
        length = self.length()
        if p2y >= p1y:
            cos = (p1x - p2x) / length
            winkel = 180 - 180 / np.pi * np.arccos(cos)
        else:
            cos = (p2x - p1x) / length
            winkel = 360 - 180 / np.pi * np.arccos(cos)

        return winkel

    def rotate(self, phi):
        """
        Erzeugt ein neues Linienobjekt, dass gegenüber diesem (self) um den Grad-Winkel phi
        gedreht ist. Es wird im den Mittelpunkt der Linie gedreht.
        :param phi: Winkel in Grad 0 <= phi < 360
        :return: Line-Objekt

        Hinweise hier:https://en.wikipedia.org/wiki/Rotation_matrix
        """

        phirad = phi * np.pi / 180

        mat = np.array([
            [np.cos(phirad), -np.sin(phirad)],
            [np.sin(phirad), np.cos(phirad)]
        ])

        center = (self.p1 + self.p2) / 2

        p1_neu = mat @ (self.p1 - center) + center
        p2_neu = mat @ (self.p2 - center) + center

        return Line(p1_neu, p2_neu)

        p1x, p1y = self.p1
        p2x, p2y = self.p2

        p1x_neu = p1x * np.cos(phirad) - p1y * np.sin(phirad)
        p1y_neu = p1x * np.sin(phirad) - p1y * np.cos(phirad)

        p2x_neu = p2x * np.cos(phirad) - p2y * np.sin(phirad)
        p2y_neu = p2x * np.sin(phirad) - p2y * np.cos(phirad)

        return Line(p1x_neu, p1y_neu), (p2x_neu, p2y_neu)

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

    l = Line((20, 30), (20, 10))
    plotline(ax, l, lw=2, label='L1')
    plotline(ax, l.rotate(120), lw=2, label='L1')
    plotline(ax, l.rotate(240), lw=2, label='L1')

    l = Line((-20, 10), (-20, 30))
    plotline(ax, l, lw=2, label='L2')
    plotline(ax, l.rotate(120), lw=2, label='L2')
    plotline(ax, l.rotate(240), lw=2, label='L2')

    plt.xlim([-40, 40])
    plt.ylim([-40, 40])
    ax.grid()
    ax.legend()
    plt.show()
