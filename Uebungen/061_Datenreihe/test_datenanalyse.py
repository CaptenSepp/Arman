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
        t = np.linspace(0, 10e-3, 1000)
        f = 1e3
        self.Vin = list(2*np.sin(2*np.pi*f*t))
        self.Vout = list(20*np.sin(2*np.pi*f*t)+30)

    def testCalc(self):
        raise NotImplementedError  # Diese Zeile bitte entfernen
#
#
#               HIER KOMMT IHRE LÖSUNG
#
#
