import numpy as np
import matplotlib.pyplot as plt

def createPlot(ax):
    """
    Plottet den Graphen, wie in der Datei graph.png.
    Es werden für jede der beiden Kurven 200 Wertepaare erzeugt.
    Beide Signale haben eine Frequenz von 2.63 MHz und eine Amplitude von 0.5mV.
    Die Linienbreite des "0°-Plots" beträgt 2. Die des anderen Plots ist 1

    WICHTIG für den Test. Als erstes den 0°-Plot ausführen!

    Schauen Sie sich für den Plot folgende Funktionen an:

    Für die Achsbeschriftungen, Legende und den Titel
    https://matplotlib.org/3.2.1/api/axes_api.html#axis-labels-title-and-legend

    Für Achscallierung und Limits
    https://matplotlib.org/3.2.1/api/axes_api.html#axis-limits-and-direction

    Für das Plotten der Funktionen
    https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
    Hierbei insbesondere die Parameter color, ls, lw und label

    :param ax: Achs-Objekt. Sie können hiermit z. B. ax.plot(...) usw. ausführen.
    :return: None
    """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


if __name__=='__main__':
    fig = plt.figure(figsize=(5, 3))
    ax = fig.gca()
    createPlot(ax)

    plt.tight_layout()
    plt.savefig('mygraph.png')

    plt.show()