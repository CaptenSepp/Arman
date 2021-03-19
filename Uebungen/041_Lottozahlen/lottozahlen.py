# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:59:27 2020
"""


def get_input(text):
    """
    Input Wrapper für die automatischen Tests NICHT VERÄNDERN

    Parameters
    ----------
    text

    Returns
    -------
    text-Input
    """
    return input(text)


def validate_input(number):
    """
    Validiert die Eingabe des Benutzers
    Erlaubt sind Zahlen von 1 bis 49 bei jeder anderen Eingabe soll False zurückgegeben werden
    Parameters
    ----------
    number: String

    Returns
    -------
    integer: if valid or bool: False if invalid input
    """
    return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def get_draw():
    """
    Generiert eine Liste mit 7 Zufallszahlen und gibt diese zurück

    Returns
    -------
    List: Liste mit 7 Zufallszahlen zwischen 1 und 49, wobei jede Zahl nur einmal in der Liste vorkommen darf
    """
    return []  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def user_input():
    """
    Nimmt 7 Zahlen als Benutzereingabe `input()` entgegen und speichert diese in einer Liste

    Zahlen:
    - dürfen nicht doppelt vorkommen
    - müssen zwischen 1 und 49 liegen
    - sollen Integer werden

    Returns
    -------
    list: Gibt eine Liste mit 7 Zahlen des Benutzers zurück
    """
    return []  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def check_numbers(numbers, tip):
    '''
    Prüft für die Listen numbers und tip wie viele "richtige" der Benutzer getippt hat

    Returns
    -------
    List: Eine Liste mit den Übereinstimmungen aus der Ziehung und den getippten Zahlen
    '''
    return 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def run():
    '''
    Es wird eine Ziehung simuliert und danach der Benutzer aufgefordert
    7 eindeutige Zahlen zwischen 1 und 49 einzugeben. Die Eingabe wird überprüft und
    das Ergenis ausgegeben.
    
    Returns
    -------
    Einen String mit den richtig getippten Zahlen:

    Es wurden folgende Zahlen gezogen: 1,2,3,4,5,6,7
    Sie haben folgende Zahlen getippt: 1,2,13,14,15,16,17
    Sie haben 2 richtige.
    '''
    numbers = get_draw()
    tip = user_input()
    result = check_numbers(numbers, tip)
    text = "Es wurden folgende Zahlen gezogen:" + str(numbers) + "\nSie haben folgende Zahlen getippt:" + str(tip) + "\nSie haben " + str(len(result)) + " richtige."
    return text


if __name__ == '__main__':
    print(run())
