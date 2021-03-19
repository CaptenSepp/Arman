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

    """
    return [' ']*9


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

    """
    if not( token == "x" or token == "o" ):
        raise ValueError("Token must be x or o")

    if not (0<=x<=2) or not (0<=y<=2):
        raise IndexError("x and or y out of range")

    index = y * 3 + x
    if playground[index] != " ":
        return False

    playground[index] = token
    return True


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

    """

    if not (0<=x<=2) or not (0<=y<=2):
        raise IndexError("x and or y out of range")

    index = y * 3 + x
    return playground[index]


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
    """

    #Zum Zeichnen einer Linie verwenden Sie bitte
    #painter.drawLine(x1, y1, x2, y2).
    #Dies Zeichnet eine Linie zwischen den Punkten (x1,y1) und (x2,y2).
    #Die Koordinaten müssen vom Typ Integer sein.

    left = int(centerx - width/2)
    right = int(centerx + width/2)
    top = int(centery - height/2)
    bot = int(centery + height/2)

    painter.drawLine(left, top, right, bot)
    painter.drawLine(left, bot, right, top)

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

    left = int(centerx - width/2)
    top = int(centery - height/2)

    painter.drawEllipse(left, top, int(width), int(height))
    pass
    



def drawEmptyPlayground(width, height, painter):
    """
    Zeichnet ein Gitter mit insgesamt 9 Kästchen.
    Die Kästchen sollen die gleiche Fläche belegen und
    insgesamt soll der gesamte Zeichenbereich der
    Breite <width> und Höhe <height> ausgenutzt werden.

    Hat der Zeichenbereich bspw. eine Breite von 7 Pixeln, dann müssen
    vier senkrechte Linien bei x=0, 2, 4, 6 erfolgen. (Feldbreite = 1 Pixel)

    0 2 4 6
    | | | |

    7 => 0, 2, 4, 6
    (7-4)/3

    Hat der Zeichenbereich bspw. eine Breite von 28 Pixeln, dann müssen
    vier senkrechte Linien bei x=0, 9, 18, 27 erfolgen. (Feldbreite = 8 Pixel)

    :param width: Breite des Zeichenbereichs (int)
    :param height: Höhe des Zeichenbereichs (int)
    :param painter: Painter-Objekt
    :return: None
    """

    for i in range(4):
        x = int( (1 + (width - 4) / 3) * i )
        painter.drawLine(x, 0, x, height-1)

    for i in range(4):
        y = int( (1 + (height - 4) / 3) * i )
        painter.drawLine(0, y, width-1, y)





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

    if not( token == ' ' or token == 'x' or token == 'o' ):
        raise ValueError()

    if token == ' ':
        return

    if token == 'x':
        painter.setPen(window.redPen)
        drawCross(centerx, centery, token_width, token_height, painter)

    if token == 'o':
        painter.setPen(window.greenPen)
        drawCircle(centerx, centery, token_width, token_height, painter)



#TODO: Spielfeld - Variable nicht global nutzen!
#TODO: Feldbreite ist nicht richtig
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
          - Feldbreite 14
!          - Die Tokenbreite soll 90% davon betragen also 0.9*15 = 13.5
!          - Die Feldmitten sind dann 7.5, 22.5, 37.5

    :param width: Breite des gesamten Spielfeldes
    :param height:  Höhe des gesamten Spielfeldes
    :param painter:  Painter Objekt
    :param window:   Window Objekt (Für die Stifte)
    :return:
    """

    painter.setPen(window.thickBlackPen)
    drawEmptyPlayground(width, height, painter)

#TODO: Bitte einmal checken mit der -4 vs -1
#    field_width = (width-4)/3
#    field_height = (height-4)/3
    field_width = (width-1)/3
    field_height = (height-1)/3

    for x in range(3): #[0, 1, 2]
        for y in range(3):
            token = getField(x, y, Spielfeld)

            centerx = (x+0.5) * field_width
            centery = (y+0.5) * field_height

            drawToken(token, centerx, centery, field_width*0.9, field_height*0.9, painter, window)

def unentschieden(field):
    '''
    Diese Funktion stellt fest, ob ein untentschieden vorliegt.
    Sie können die Felder mit getField(x,y, field) abfragen.
    :param field: Datenstruktur des Spielfeldes
    :return:
        True: Untentschieden
        False: Nicht unentschieden
    '''

    for x in range(3): #[0, 1, 2]
        for y in range(3):
            token = getField(x, y, field)
            if token == ' ':
                return False

    if gewinner(field) is None:
        return True
    else:
        return False


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

    def checkTokens(tokens):
        if tokens[0]==tokens[1] and tokens[0]==tokens[2]:
            if (tokens[0]=='x'):
                return 'x'
            if (tokens[0]=='o'):
                return 'o'
        return None

    for y in range(3):
        tokens = [getField(x, y, field) for x in range(3)]  # ['x', 'x', 'x']
        result = checkTokens(tokens)
        if result is not None:
            return result

    for x in range(3):
        tokens = [getField(x, y, field) for y in range(3)]  # ['x', 'x', 'x']
        result = checkTokens(tokens)
        if result is not None:
            return result

    tokens = [getField(i, i, field) for i in range(3)]  # ['x', 'x', 'x']
    result = checkTokens(tokens)
    if result is not None:
        return result

    tokens = [getField(2-i, i, field) for i in range(3)]  # ['x', 'x', 'x']
    result = checkTokens(tokens)
    if result is not None:
        return result

    return None

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

#    mousex / (width/3)  #Werte zwischen 0 und 2.999, weil mousex=0...width-1
    x = int(mousex / (width/3)) #0, 1, 2
    y = int(mousey / (height/3)) #0, 1, 2

    return x,y

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    