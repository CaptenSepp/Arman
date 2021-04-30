# -*- coding: utf-8 -*-

import math
import re


def element_is_not_float(param):
    try:
        float(param)
        return False
    except ValueError:
        return True


def remove_string_from_list(list):
    i = 0
    while i < len(list):
        if element_is_not_float(list[i]):
            list.pop(i)
            continue
        i += 1
    return list


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

    list = re.split(r'[,\s+\']', zahlenstring)
    list = remove_string_from_list(list)
    result = sum(map(float, list))
    return result


#######################################
#        AB HIER NICHTS MEHR ÄNDERN
#######################################

if __name__ == '__main__':
    import gui

    gui.run(berechnung)
