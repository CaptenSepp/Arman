#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:49:00 2020

@author: student
"""


def tageszeit(uhrzeit):
    """
    Gibt die Zeichenketten "Nacht" und "Nicht Nacht" abhängig von
    der Uhrzeit aus. Nacht ist von 22:00 - 05:00

    Parameters
    ----------
    uhrzeit : str
        Die Uhrzeit als String in der Form HH:MM

    Returns
    -------
    String mit der Tageszeit (siehe oben)

    """
    """
    zeit = [int(x) for x in uhrzeit.split(':')]
    min = zeit[0]*60 + zeit[1]

    if (min >= 60*22) or (min <= 60*5):
        result = "Nacht"
    else:
        result = "Nicht Nacht"

    return result
    """
    h, _ = [int(x) for x in uhrzeit.split(':')]
    if (5<h<22):
        return "Nicht Nacht"
    else:
        return "Nacht"


if __name__ == '__main__':
    print(tageszeit("03:06"))
    print(tageszeit("13:32"))
    print(tageszeit("22:06"))
