# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:57:32 2020
"""


import unittest
import numpy as np

import sys
import os
sys.path.insert(0, os.path.split(__file__)[0])

from Uebung_sinus import *



class Test(unittest.TestCase):
    def test1(self):
        result = sinusliste(0, 3, 1)
        expected = [[0, 0.0], 
                    [1, 0.8414709848078965], 
                    [2, 0.9092974268256817], 
                    [3, 0.1411200080598672]]
        
        result = np.array(result)
        expected = np.array(expected)
        np.testing.assert_almost_equal(result, expected)
        
    def test2(self):
        result = sinusliste(1, 1.5, .1)
        expected = [[1, 0.8414709848078965], 
                    [1.1, 0.8912073600614354], 
                    [1.2000000000000002, 0.9320390859672264], 
                    [1.3000000000000003, 0.9635581854171931], 
                    [1.4000000000000004, 0.9854497299884603]]
        
        result = np.array(result)
        expected = np.array(expected)
        np.testing.assert_almost_equal(result, expected)

    def test3(self):
        result = sinusliste(1.5, 1, .1)
        expected = []
        
        result = np.array(result)
        expected = np.array(expected)
        np.testing.assert_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()