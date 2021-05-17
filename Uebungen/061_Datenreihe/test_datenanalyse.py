import unittest
import os
import datenanalyse as MUT
import numpy as np

class testReadData(unittest.TestCase):
    def setUp(self) -> None:
        self.fn = 'testdatafile.txt'
        with open(self.fn, 'w') as fd:
            fd.write("a\tb\tc\n")
            fd.write("1\t2\t3\n")
            fd.write("1e-3\t5e-2\t-0.0001\n")

        self.fnError = 'testdatafileNotExisting.txt'

    def tearDown(self) -> None:
        os.unlink(self.fn)

    def testRead(self):
        raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


    def testReadNotExisting(self):
        raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#


class testExtractData(unittest.TestCase):
    def setUp(self) -> None:
        self.datalines = ["a\tV(in)\tV(out)\n", "1\t2\t3\n", "1e-3\t5e-2\t-0.0001\n"]

    def testCorrectExtraction(self):
        raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#

class testCalcAmplification(unittest.TestCase):
    def setUp(self) -> None:
        v = np.array([0, 0, -1, 1, 0, 0, -1, -1, 1, 1])
        self.Vin = list(2*v)
        self.Vout = list(20*v+30)

    def testCalc(self):
        raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
