#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:53:57 2020

@author: student
"""

import sys
import os
sys.path.insert(0, os.path.split(__file__)[0])

from tageszeiten1 import *

    
import unittest

class TestTageszeiten(unittest.TestCase):
    def test_nacht(self):
        self.assertEqual(tageszeit("03:06"), "Nacht")
        self.assertEqual(tageszeit("00:00"), "Nacht")
        self.assertEqual(tageszeit("23:06"), "Nacht")

    def test_morgen(self):
        self.assertEqual(tageszeit("05:00"), "Morgen")
        self.assertEqual(tageszeit("08:06"), "Morgen")
        self.assertEqual(tageszeit("10:59"), "Morgen")

    def test_mittag(self):
        self.assertEqual(tageszeit("11:00"), "Mittag")
        self.assertEqual(tageszeit("12:06"), "Mittag")
        self.assertEqual(tageszeit("12:59"), "Mittag")

    def test_nachmittag(self):
        self.assertEqual(tageszeit("13:00"), "Nachmittag")
        self.assertEqual(tageszeit("15:16"), "Nachmittag")
        self.assertEqual(tageszeit("16:59"), "Nachmittag")

    def test_abend(self):
        self.assertEqual(tageszeit("17:00"), "Abend")
        self.assertEqual(tageszeit("19:56"), "Abend")
        self.assertEqual(tageszeit("22:29"), "Abend")

    def test_illegal_clock(self):
        with self.assertRaises(ValueError):
            tageszeit("55:22")

    def test_illegal_clock1(self):
        with self.assertRaises(ValueError):
            tageszeit("5:22")

    def test_illegal_clock2(self):
        with self.assertRaises(ValueError):
            tageszeit("05-22")

if __name__ == '__main__':
    unittest.main()