# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:47:20 2020

@author: torsten
"""


def mapping(coordinate, src_minmax, dest_minmax):
    """
    Wandelt die 1D Koordinate <coordinate> von einem Koordinatensystem (src)
    in ein anderes System (dest).
    
    So ergibt z. B. 
        mapping(244, [244, 268], [-100, 100]) ==> -100
        mapping(268, [244, 268], [-100, 100]) ==> 100

    Parameters
    ----------
    coordinate : float
        Quellkoordinate
    src_minmax : Liste mit 2 Einträgen (min, max)
        [min, max]
    dest_minmax : Liste mit 2 Einträgen (min, max)
        [min, max]

    Returns
    -------
    1D Koordinate im Zielkoordinatensystem

    """
    
