# -*- coding: utf-8 -*-

import math

def berechnung(radius):
    return radius**2 * math.pi


#######################################
#        AB HIER NICHTS MEHR ÄNDERN
#######################################

if __name__ == '__main__':
    import gui
    gui.run(berechnung)
