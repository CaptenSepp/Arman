import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import numpy as np

from konto import Konto

class testKonto(unittest.TestCase):
    def testCreate(self):
        k = Konto(anfangswert = 0, zins = 1)
        self.assertAlmostEqual(k.stand(), 0)

    def testEinzahlung(self):
        k = Konto(anfangswert = 0, zins = 1)
        k.einzahlung(3)
        k.einzahlung(7)
        self.assertAlmostEqual(k.stand(), 10)

    def testEinzahlung1(self):
        k = Konto(anfangswert = 0, zins = 1)
        with self.assertRaises(ValueError):
            k.einzahlung(-7)

    def testAuszahlung1(self):
        k = Konto(anfangswert = 100)
        z = k.auszahlung(30)

        self.assertAlmostEqual(z, 30)
        self.assertAlmostEqual(k.stand(), 70)

    def testAuszahlung2(self):
        k = Konto(anfangswert = 100)
        z = k.auszahlung(300)

        self.assertAlmostEqual(z, 100)
        self.assertAlmostEqual(k.stand(), 0)

    def testAuszahlung3(self):
        k = Konto(anfangswert = 100, dispogrenze = 500)
        z = k.auszahlung(1000)

        self.assertAlmostEqual(z, 600)
        self.assertAlmostEqual(k.stand(), -500)

    def testAuszahlung4(self):
        k = Konto(anfangswert = -600, dispogrenze = 500)
        z = k.auszahlung(1000)

        self.assertAlmostEqual(z, 0)
        self.assertAlmostEqual(k.stand(), -600)

    def testAuszahlung5(self):
        k = Konto(anfangswert = -600, dispogrenze = 500)

        with self.assertRaises(ValueError):
            z = k.auszahlung(-1000)

            
    def testZins1(self):
        k = Konto(anfangswert = 100, zins=5)

        k.periodenAbschluss()
        self.assertAlmostEqual(k.stand(), 105)

        k.periodenAbschluss()
        self.assertAlmostEqual(k.stand(), 110.25)

    def testSparplan(self):
        k = Konto(zins=2)

        k.sparPlan(K=100, N=12)

        self.assertAlmostEqual(k.stand(), 1368.0331522689812)

    def testSparplan1(self):
        k = Konto()
        with self.assertRaises(ValueError):
            k.sparPlan(N=-1, K=0)

    def testSparplan2(self):
        k = Konto()
        with self.assertRaises(ValueError):
            k.sparPlan(N=1, K=-1)

    def testSparplan3(self):
        k = Konto(zins=5)
        k.sparPlan(N=0, K=1000)
        self.assertAlmostEqual(k.stand(), 0)
