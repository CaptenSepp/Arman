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
    return [" "] * 9


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
    """

    if x not in [0, 1, 2] or y not in [0, 1, 2]:
        raise IndexError("y oder x ausßerhalb des gültigen Bereichs")
    if token not in ["x", "o"]:
        raise ValueError("token ausßerhalb des gültigen Beträge")

    index = 3 * y + x
    if playground[index] == " ":
        playground[index] = token
        return True
    else:
        return False

    # Represents the Tic Tac Toe
    # values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    # player_pos = {'X': [], 'O': []}


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
    """
    if playground[x][y] == "":
        return " "
    return playground[x][y]


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
    painter.drawLine(centerx - width / 2, centery + height / 2, centerx + width / 2, centery - height / 2)
    painter.drawLine(centerx - width / 2, centery - height / 2, centerx + width / 2, centery + height / 2)
    # Die Koordinaten müssen vom Typ Integer sein.


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
    painter.drawEllipse(centerx, centery, width, height)


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
    painter.drawLine(width / 3, height, width / 3, 0)
    painter.drawLine(2 * width / 3, height, 2 * width / 3, 0)
    painter.drawLine(width, height / 3, 0, height / 3)
    painter.drawLine(width, 2 * height / 3, 0, 2 * height / 3)


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
    ***********************************************************************************************
    """
    if token == "x":
        painter.setPen(window.redPen)
        drawCross(centerx, centery, token_width, token_height)
    elif token == "o":
        painter.setPen(window.greenPen)
        drawCircle(centerx, centery, token_width, token_height)
    elif not token == " ":
        raise ValueError
    return None


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


def are_all_cells_filled(field):


def unentschieden(field):
    '''
    Diese Funktion stellt fest, ob ein untentschieden vorliegt.
    Sie können die Felder mit getField(x,y, field) abfragen.
    :param field: Datenstruktur des Spielfeldes
    :return:
        True: Untentschieden
        False: Nicht unentschieden
    '''

    for i in range(3):
        for j in range(3):
            token = getField(i, j, field)
            if token == " ":
                return False

    winner = gewinner(field)

    if winner in ["x", "y"]:
        return False
    else:
        return True


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
    tokens = "".join([getField(i, i, field) for i in range(3)])
    if tokens == "xxx" or tokens == "ooo":
        return tokens[0]

    tokens = "".join([getField(i, 2 - i, field) for i in range(3)])
    if tokens == "xxx" or tokens == "ooo":
        return tokens[0]

    #Vertikal
    for x in range(3):
        tokens = "".join([getField(x, y, field) for y in range(3)])
        if tokens == "xxx" or tokens == "ooo":
            return tokens[0]
    #Horizontal
    for y in range(3):
        tokens = "".join([getField(x, y, field) for y in range(3)])
        if tokens == "xxx" or tokens == "ooo":
            return tokens[0]


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
    ix = iy = 0
    if mousex < width / 3:
        ix = 0
    elif width / 3 < mousex < 2 * width / 3:
        ix = 1
    elif 2 * width / 3 < mousex:
        ix = 2
    if mousey < height / 3:
        iy = 0
    elif height / 3 < mousey < 2 * height / 3:
        iy = 1
    elif 2 * height / 3 < mousey:
        iy = 2
    return ix, iy


#########################################################
#         AB HIER NICHTS MEHR ÄNDERN
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

    gui.run(callback_repaint=repaint, callback_init=init, callback_mouseclick=mouseclick)
