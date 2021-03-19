#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:53:57 2020

@author: student
"""

import sys
import os
sys.path.insert(0, os.path.split(__file__)[0])

from tageszeiten import *

    
import unittest

class TestTageszeiten(unittest.TestCase):
    def test_nacht(self):
        self.assertEqual(tageszeit("03:06"), "Nacht")
        self.assertEqual(tageszeit("00:00"), "Nacht")
        self.assertEqual(tageszeit("23:06"), "Nacht")
    def test_nicht_nacht(self):
        self.assertEqual(tageszeit("06:00"), "Nicht Nacht")
        self.assertEqual(tageszeit("21:59"), "Nicht Nacht")
        self.assertEqual(tageszeit("13:06"), "Nicht Nacht")



if __name__ == '__main__':
    unittest.main()