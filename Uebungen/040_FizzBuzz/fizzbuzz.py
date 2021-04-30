# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:59:27 2020
"""


def fizzbuzzNumber(number):
    """
    Prüft für eine Zahl, ob Sie durch 3 und oder 5 teilbar ist.

    Parameters
    ----------
    number : int
        Die zu prüfende Zahl

    Returns
    -------
    'Fizz', wenn number durch 3 teilbar
    'Buzz', wenn number durch 5 teilbar
    'FizzBuzz', wenn number durch 3 und 5 teilbar
    Sonst die Zahl selber als String
    """

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)


def run():
    '''
    Für alle Zahlen von 1-100 wird die jeweilige Ausgabe unter
    Nutzung der Funktion fizzbuzzNumber(...) erzeugt.
    
    Returns
    -------
    Einen String mit der Auflistung aller Zahlen und mit 10 Zahlen pro Zeile.
    Trennung erfolgt mit Komma und Leerzeichen: "1, 2, Fizz, 4"
    Nach der letzten Zeile erfolgt ein Zeilenumbruch.
    '''

    result = ""
    j = 0
    for i in range(1, 101):
        j += 1
        if j == 10:
            result += str(fizzbuzzNumber(i)) + "\n"
            j = 0
            continue
        result += str(fizzbuzzNumber(i)) + ", "
    return result


if __name__ == '__main__':
    run()






