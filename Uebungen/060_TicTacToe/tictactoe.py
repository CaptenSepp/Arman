# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:20:23 2020

@author: torsten
"""

from itertools import product

def createEmptyPlayground():
    """
    Die Funktion erstellt die Repräsentation eines leeren Spielfeldes mit
    3x3 Feldern.
    
    Die Felder werden als einzelne Strings mit dem Inhalt ' ' oder 'o' oder 'x'
    in einer Liste mit 9 Einträgen abgelegt. Die 9 Einträge ergeben
    sich aus dem zeilenweisen hintereinanderschreiben der Felder.
    
    

    Returns
    -------
    Liste mit 9 Einträgen
    *************************************************************************************************************************
    inja mige ye array besaz (list) ke 9 ta khune dashte bashe (albate jolo tar mige bayad 3*3 bashe benazaram) 
    baad bayad return beshe
    """
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
    
    return []  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def setField(x, y, token, playground):
    """
    Setzt an der Position x,y auf dem Spielfeld den 
    Spielstein <token>, wenn das Feld frei ist.
    
    Wenn die Position nicht innerhalb des Spielfeldes liegt, wird
    ein IndexError geworfen.
    
    Wenn das Token nicht x oder o ist, dann wird ein ValueError geworfen.

    Parameters
    ----------
    x : int 
        Position in X (0,1,2)
    y : int
        Position in Y (0,1,2)
    token : str
        Der Spielstein "x" oder "o"
    playground : 
        Die Datenstruktur des Spielfeldes

    Returns
    -------
    True, wenn Spielstein gesetzt wurde
    False, wenn Spielstein aufgrund eines besetzten Feldes nicht gesetzt wurde
    *************************************************************************************************************************
    int x: 0,1,2 mishe
    int y: 0,1,2 mishe
    ye stringam ke mishe x ya o ke bayad ehtemalan jaye khune habeshe
    hamun bazie dooze khodemune
    ye "playground" ham hast behesh mige (data structure), ino nemidunam chiye, miduni?
    
    """
    
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
    
    return False  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def getField(x, y, playground):
    """
    Gibt den Spielstein (token) oder ' ' als leeres Feld
    der Position x,y auf dem Spielfield zurück

    Wenn die Position nicht innerhalb des Spielfeldes liegt, wird
    ein IndexError geworfen.
    

    Parameters
    ----------
    x : int 
        Position in X (0,1,2)
    y : int
        Position in Y (0,1,2)
    playground : 
        Die Datenstruktur des Spielfeldes

    Returns
    -------
    'x', 'o', ' '
    *************************************************************************************************************************
    injam ke getter wase hanun dade hast, ke ehtemalan bayad bege ke in khune pore ya mishe chizi jash gozasht
    ke return mikone "x" , "o", " " ke yani jaye khali
    playgroun ham return nemikone faghat estefade mikone
    """

    return ' '  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def drawCross(centerx, centery, width, height, painter):
    """
    Zeichnet ein Kreuz mit zwei diagonalen Linien in das Rechteck, welches
    durch Mitte (centerx, centery) und Breite, Höhe (width, height)
    beschrieben wird.

    :param centerx: X-Koordinate der Rechteckmitte (float)
    :param centery: Y-Koordinate der Rechteckmiite (float)
    :param width:   Breite des Rechtecks (float)
    :param height:  Höhe des Rechtecks (float)
    :param painter: Painter-Objekt
    :return: None
    *************************************************************************************************************************
    """

    #Zum Zeichnen einer Linie verwenden Sie bitte
    #painter.drawLine(x1, y1, x2, y2).
    #Dies Zeichnet eine Linie zwischen den Punkten (x1,y1) und (x2,y2).
    #Die Koordinaten müssen vom Typ Integer sein.

#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def drawCircle(centerx, centery, width, height, painter):
    """
    Zeichnet eine Ellipse in das Rechteck, welches
    durch Mitte (centerx, centery) und Breite, Höhe (width, height)
    beschrieben wird. Das Rechteck soll oben, unten und links, rechts berührt werden.

    :param centerx: X-Koordinate der Rechteckmitte (float)
    :param centery: Y-Koordinate der Rechteckmiite (float)
    :param width:   Breite der Ellipse (float)
    :param height:  Höhe der Ellipse (float)
    :param painter: Painter-Objekt
    :return: None
    """

    # Zum Zeichnen einer Ellipse verwenden Sie bitte
    # painter.drawEllipse(x, y, w, h)
    # Dies zeichnet eine Ellipse in das Rechteck (x,y) - (x+w, y+h)

#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
    



def drawEmptyPlayground(width, height, painter):
    """
    Zeichnet ein Gitter mit insgesamt 9 Kästchen.
    Die Kästchen sollen die gleiche Fläche belegen und
    insgesamt soll der gesamte Zeichenbereich der
    Breite <width> und Höhe <height> ausgenutzt werden.

    Hat der Zeichenbereich bspw. eine Breite von 7 Pixeln, dann müssen
    vier senkrechte Linien bei x=0, 2, 4, 6 erfolgen. (Feldbreite = 1 Pixel)

    Hat der Zeichenbereich bspw. eine Breite von 28 Pixeln, dann müssen
    vier senkrechte Linien bei x=0, 9, 18, 27 erfolgen. (Feldbreite = 8 Pixel)

    :param width: Breite des Zeichenbereichs (int)
    :param height: Höhe des Zeichenbereichs (int)
    :param painter: Painter-Objekt
    :return: None
    """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def drawToken(token, centerx, centery, token_width, token_height, painter, window):
    """
    Zeichnet die Token auf den Bildschirm.
    Verwendung bei <token>='x' von drawCross und bei 'o' von drawCircle!
    Vor dem Aufruf der Zeichenfunktion wählen Sie bitte den Zeichenstift mit
    painter.setPen( window.redPen ) für 'x'
    oder painter.setPen( window.greenPen ) für 'o'
    aus.

    Wenn ein ungültiger token übergeben wird, dann muss ein ValueError geworfen werden.

    :param token: ' ', 'x' oder 'o'
    :param centerx: Zentrum des Feldes, in das der Token gezeichnet wird
    :param centery: Zentrum des Feldes, in das der Token gezeichnet wird
    :param token_width: Breite des Feldes
    :param token_height: Breite des Feldes
    :param painter: Painter Objekt
    :param window:  Winows Objekt (Hier sind z. B. die Stiftfarben gespeichert)
    :return: None
    """
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


def repaint(width, height, painter, window):
    """
    In dieser Funktion wird das Spielfeld gezeichnet.
    Das Vorgehen ist folgendes:
        * Zeichnen eines leeren Spielfeldes mit drawEmptyPlayground in Schwarz (Auswahl des Stifts mit painter.setPen(window.thickBlackPen)
        * Aufruf der funktion drawToken für alle 9 Felder. Dabei den entsprechenden Token mit getField abfragen.


    Jedes Token wird in die Mitte des jeweiligen Feldes gezeichnet.
    Dabei hat das Token genau 90% der Breite bzw. Höhe des Spielfeldes.
    Beispiel eines Spieldfeldes der Breite 46 (Angabe nur für die X-Achse. Y-Achse entsprechend)
          - Senkrechte Linien bei 0, 15, 30, 45
          - Feldbreite 15
          - Die Tokenbreite soll 90% davon betragen also 0.9*15 = 13.5
          - Die Feldmitten sind dann 7.5, 22.5, 37.5

    :param width: Breite des gesamten Spielfeldes
    :param height:  Höhe des gesamten Spielfeldes
    :param painter:  Painter Objekt
    :param window:   Window Objekt (Für die Stifte)
    :return:
    """

#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def unentschieden(field):
    '''
    Diese Funktion stellt fest, ob ein untentschieden vorliegt.
    Sie können die Felder mit getField(x,y, field) abfragen.
    :param field: Datenstruktur des Spielfeldes
    :return:
        True: Untentschieden
        False: Nicht unentschieden
    '''

    return False  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def gewinner(field):
    '''
    Diese Funktion stellt fest, ob ein Gewinn vorliegt.
    Sie können die Felder mit getField(x,y, field) abfragen.
    :param field: Datenstruktur des Spielfeldes
    :return:
        'x': X hat gewonnen
        'o': O hat gewonnen
        None: niemand hat gewonnen
    '''

#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

def mapMouseToField(mousex, mousey, width, height):
    '''
    Diese Funktion berechnet aus einer Mauskoordinate die Feldposition mit
    ix = 0,1,2 und iy=0,1,2

    :param mousex: Mauskoordinate
    :param mousey: Mauskoordinate
    :param width:  Breite des gesamten Spieldfeldes
    :param height:  Höhe des gesamten Spielfeldes
    :return: ix, iy als integer
    '''
    return 0, 0  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

#########################################################
#########################################################
#########################################################
#         AB HIER NICHTS MEHR ÄNDERN
#########################################################
#########################################################
#########################################################

Spielfeld = None
tokens = "xo"
current = 0

def init(window):
    global Spielfeld
    global current

    current = 0
    Spielfeld = createEmptyPlayground()
    window.setStatus("Das {} ist dran...".format(tokens[current]))


def mouseclick(x, y, width, height, window):
    global current

    if gewinner(Spielfeld):
        return

    ix, iy = mapMouseToField(x, y, width, height)
    ok = setField(ix, iy, tokens[current], Spielfeld)

    if ok:
        current = (current + 1) % 2
        window.setStatus("Das {} ist dran...".format(tokens[current]))
    else:
        window.setStatus("Bitte auf ein freies Feld drücken.")

    who = gewinner(Spielfeld)
    if who is not None:
        window.setStatus("{} hat gewonnen!".format(who))
    elif unentschieden(Spielfeld):
        window.setStatus("unentschieden")
        return


if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    import gui
    
    gui.run(callback_repaint = repaint, callback_init = init, callback_mouseclick = mouseclick)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
