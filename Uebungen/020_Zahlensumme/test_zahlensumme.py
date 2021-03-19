# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:18:53 2020

@author: torsten
"""
import sys
import os
sys.path.insert(0, os.path.split(__file__)[0])

from zahlensumme import *

import unittest

class Test(unittest.TestCase):
    def test_formular(self):
        self.assertAlmostEqual(berechnung("20,5"), 25)
        self.assertAlmostEqual(berechnung("20.12   ,  5e2"), 520.12)
        self.assertAlmostEqual(berechnung(""), 0)
        self.assertAlmostEqual(berechnung("  "), 0)
        self.assertAlmostEqual(berechnung(" 5, -13 "), -8)

if __name__ == '__main__':
    unittest.main()