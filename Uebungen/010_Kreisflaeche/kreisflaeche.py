# -*- coding: utf-8 -*-

import math


def berechnung(radius):
    return (math.pi * radius ** 2)


#######################################
#        AB HIER NICHTS MEHR ÄNDERN
#######################################

if __name__ == '__main__':
    import gui

    gui.run(berechnung)
