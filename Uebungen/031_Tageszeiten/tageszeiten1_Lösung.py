#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:49:00 2020

@author: student
"""


def tageszeit(uhrzeit):
    """
    Gibt die Tageszeit entsprechend der Uhrzeit als String zurück.

    Uhrzeit        Rückgabe
    00:00 - 04:59  Nacht
    05:00 - 10:59  Morgen
    11:00 - 12:59  Mittag
    13:00 - 16:59  Nachmittag
    17:00 - 22:29  Abend
    22:30 - 23:59  Nacht

    Wenn die Uhrzeit nicht dem Format HH:MM entspricht, wird eine ValueError-Exception erzeugt
    --- Beispiel dafür "raise ValueError("Falsches Format")

    Parameters
    ----------
    uhrzeit : str
        Die Uhrzeit als String in der Form HH:MM

    Returns
    -------
    String mit der Tageszeit (siehe oben)

    """

    zeit = uhrzeit.replace(':', '')
    valide_zeit = int(zeit)

    if len(zeit) == 4:
        if 0 <= valide_zeit < 500 or 2230 <= valide_zeit <= 2359:
            return ("Nacht")

        elif 500 <= valide_zeit <= 1059:
            return ("Morgen")

        elif 1100 <= valide_zeit <= 1259:
            return ("Mittag")

        elif 1300 <= valide_zeit <= 1659:
            return ("Nachmittag")

        elif 1700 <= valide_zeit <= 2229:
            return ("Abend")

        else:
            raise ValueError

    else:
        raise ValueError


if __name__ == '__main__':
    print(tageszeit("03:06"))
    print(tageszeit("13:32"))
    print(tageszeit("22:06"))
