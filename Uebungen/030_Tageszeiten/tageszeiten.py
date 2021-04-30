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
    splited_uhrzeit = uhrzeit.split(":")
    hhmm = int(splited_uhrzeit[0] + splited_uhrzeit[1])
    if 2200 < hhmm < 2359 or 0000 <= hhmm < 500:
        return "Nacht"
    return "Nicht Nacht"


if __name__ == '__main__':
    print(tageszeit("03:06"))
    print(tageszeit("13:32"))
    print(tageszeit("22:06"))
