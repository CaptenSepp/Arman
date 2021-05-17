# -*- coding: utf-8 -*-

import math

def berechnung(zahlenstring):
    '''
    Parameters
    ----------
    zahlenstring : str
        Dies ist der String, der im Textfeld eingegeben wurde.
        Die Zahlen sind mit Komma getrennt. Leerzeichen können auftauchen.

    Returns
    -------
    float oder int mit der Summe der Zahlen

    '''

    zahlenliste = zahlenstring.split(',')

    summe = 0.0
    for zahl in zahlenliste:
        try:
            summe += float(zahl)
        except ValueError:
            pass

    return summe


#######################################
#        AB HIER NICHTS MEHR ÄNDERN
#######################################

if __name__ == '__main__':
    import gui
    gui.run(berechnung)
