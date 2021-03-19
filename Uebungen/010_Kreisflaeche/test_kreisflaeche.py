# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:18:53 2020

@author: torsten
"""

import sys
import os

import kreisflaeche as DUT

import unittest

class Test(unittest.TestCase):
    def test_formular(self):
        self.assertAlmostEqual(DUT.berechnung(1), 3.141592653589793)
        self.assertAlmostEqual(DUT.berechnung(3), 28.274333882308138)

if __name__ == '__main__':
    unittest.main()