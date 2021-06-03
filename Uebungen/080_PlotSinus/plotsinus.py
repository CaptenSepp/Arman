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

    phi1_deg = 0
    phi2_deg = 35
    phi1 = phi1_deg / 180 * np.pi
    phi2 = phi2_deg / 180 * np.pi
    f = 2.63e6
    a = 0.5
    t = np.linspace(0, 1e-6, 200)

    y1 = a * np.sin(2 * np.pi * f * t - phi1)
    y2 = a * np.sin(2 * np.pi * f * t - phi2)

    ax.plot(t * 1e6, y1, color='k',
            label='{:.2f} MHz mit {:.0f}° Phasenverschiebung'.format(f / 1e6, phi1_deg),
            ls='-', lw=2)
    ax.plot(t * 1e6, y2, color='k',
            label='{:.2f} MHz mit {:.0f}° Phasenverschiebung'.format(f / 1e6, phi2_deg),
            ls='--', lw=1)
    ax.legend(loc='upper left')
    ax.grid()
    ax.set_title('Zwei versetzte Sinussignale')
    ax.set_ylim([-1.5, 2.0])
    ax.set_ylabel('Amplitude in mV')
    ax.set_xlabel('Zeit in us')



if __name__ == '__main__':
    fig = plt.figure(figsize=(5, 3))
    ax = fig.gca()
    createPlot(ax)

    plt.tight_layout()
    plt.savefig('mygraph.png')

    plt.show()
