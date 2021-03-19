# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:57:32 2020

@author: torsten
"""


import unittest

import sys
import os
sys.path.insert(0, os.path.split(__file__)[0])

from Uebung_mapping import *

class Test(unittest.TestCase):
    def test_min1(self):
        v = mapping(244, [244, 2168], [-100, 100])
        self.assertAlmostEqual(v, -100)

    def test_min2(self):
        v = mapping(244, [244, 218], [-100, 100])
        self.assertAlmostEqual(v, -100)
        
    def test_max1(self):
        v = mapping(588, [21, 588], [-100, 100])
        self.assertAlmostEqual(v, 100)

    def test_max2(self):
        v = mapping(268, [2441, 268], [-100, 100])
        self.assertAlmostEqual(v, 100)



if __name__ == '__main__':
    unittest.main()