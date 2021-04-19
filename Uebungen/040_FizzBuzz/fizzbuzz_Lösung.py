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
    
    fizz = (number % 3 == 0)
    buzz = (number % 5 == 0)

    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
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
    
    result = ''
    for x in range(1, 101):
        result += fizzbuzzNumber(x)
        if x % 10 == 0:
            result += '\n'
        else:
            result += ', '

    return result
    
    
if __name__ == '__main__':
    print( run() )
    

        
