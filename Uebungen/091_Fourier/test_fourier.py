import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import shutil
import os


from fourier import Creator, Analyzer

class testCreator_evaluate(unittest.TestCase):
    def setUp(self):
        self.mut = Creator()


    def testCorrectLength(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='t')
        t, y = self.mut.evaluate()
        self.assertIsInstance(t, np.ndarray)

        self.assertEqual(t.shape, y.shape)
        self.assertEqual(100, len(t))

    def testCorrectLength1(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1238, Ausgabedatei='', Ausdruck='t')
        t, y = self.mut.evaluate()
        self.assertIsInstance(t, np.ndarray)

        self.assertEqual(t.shape, y.shape)
        self.assertEqual(123, len(t))

    def testCorrectDeltaTime(self):
        self.mut.set(Abtastfrequenz=10, Dauer=2, Ausgabedatei='', Ausdruck='t')
        t, y = self.mut.evaluate()
        self.assertIsInstance(t, np.ndarray)

        dt = t[1]-t[0]
        self.assertAlmostEqual(0.1, dt)

    def testCorrectTimeLimits(self):
        self.mut.set(Abtastfrequenz=10, Dauer=1, Ausgabedatei='', Ausdruck='t')
        t, y = self.mut.evaluate()
        self.assertIsInstance(t, np.ndarray)

        self.assertEqual(0, t[0])
        self.assertEqual(0.9, t[-1])

    def testCorrectExprEval(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='t')
        t, y = self.mut.evaluate()
        self.assertIsInstance(t, np.ndarray)

        self.assertAlmostEqual(t[0], 0)
        np.testing.assert_array_almost_equal(t, y)

    def testCorrectExprEval1(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='sin(t)**2 + cos(2*pi*100*t)')
        t, y = self.mut.evaluate()

        self.assertIsInstance(t, np.ndarray)
        exp = np.sin(t)**2 + np.cos(2*np.pi*100*t)
        np.testing.assert_array_almost_equal(exp, y)

    def testExprError(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='sin(t)**2 + cos(2*pi*100*x)')

        with self.assertRaises(NameError):
            t, y = self.mut.evaluate()

    def testExprEmpty(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='')

        with self.assertRaises(SyntaxError):
            t, y = self.mut.evaluate()

    def testExprError1(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='sin(2t)')

        with self.assertRaises(SyntaxError):
            t, y = self.mut.evaluate()

    def testExprDivZero(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=0.1, Ausgabedatei='', Ausdruck='t/0')

        with self.assertRaises(KeyError):
            t, y = self.mut.evaluate()

class testCreator_excel(unittest.TestCase):
    def setUp(self):
        self.mut = Creator()

    def doCleanups(self):
        try:
            os.remove('testoutput.xlsx')
        except FileNotFoundError:
            pass

    def test_write1(self):
        self.mut.set(Abtastfrequenz=1000, Dauer=10e-3, Ausgabedatei='testoutput.xlsx', Ausdruck='2*t')


        t, y = self.mut.evaluate()
        self.mut.writeToExcel(t, y)

        self.assertTrue(os.path.exists('testoutput.xlsx'))
        df = pd.read_excel('testoutput.xlsx')

        self.assertIn('t', df.columns)
        self.assertIn('y', df.columns)
        np.testing.assert_array_almost_equal(t, df.t.to_numpy())
        np.testing.assert_array_almost_equal(y, df.y.to_numpy())

class testAnalyzer_excel(unittest.TestCase):
    def setUp(self):
        self.mut = Analyzer()

    def doCleanups(self):
        try:
            os.remove('testoutput.xlsx')
        except FileNotFoundError:
            pass

    def test_read1(self):
        t = np.linspace(0, 10, 100)
        y = t * 9
        df = pd.DataFrame({'t':t, 'y':y})
        df.to_excel('testoutput.xlsx')

        self.mut.set(Eingabedatei='testoutput.xlsx', ax1=None, ax2=None)
        exp_t, exp_y = self.mut.readData()

        np.testing.assert_array_almost_equal(exp_t, t)
        np.testing.assert_array_almost_equal(exp_y, y)

    def test_correctReturnType(self):
        t = np.linspace(0, 10, 100)
        y = t * 9
        df = pd.DataFrame({'t':t, 'y':y})
        df.to_excel('testoutput.xlsx')

        self.mut.set(Eingabedatei='testoutput.xlsx', ax1=None, ax2=None)
        exp_t, exp_y = self.mut.readData()
        #TODO: auch Serien gehen hier durch
        self.assertIsInstance(exp_t, np.ndarray)
        self.assertIsInstance(exp_y, np.ndarray)


class testAnalyzer_calcFourierCoefficients(unittest.TestCase):
    def setUp(self):
        self.mut = Analyzer()

        t = np.linspace(0, 10e-3, 100, endpoint=False)
        y = np.sin(2*np.pi*t*1000) + 2*np.sin(2*np.pi*t*2000)
        f, c = self.mut.calcFourierCoefficients(t, y)

        self.tyfc = (t, y, f, c)

    def testCorrectFrequenciesCount(self):
        t, y, f, c = self.tyfc
        self.assertEqual(51, len(f))

    def testCorrectReturnType(self):
        t, y, f, c = self.tyfc
        self.assertIsInstance(t, np.ndarray)
        self.assertIsInstance(y, np.ndarray)
        self.assertIsInstance(f, np.ndarray)
        self.assertIsInstance(c, np.ndarray)

    def testCorrectStartFrequency(self):
        t, y, f, c = self.tyfc
        self.assertEqual(0, f[0])

    def testCorrectEndFrequency(self):
        t, y, f, c = self.tyfc
        self.assertEqual(5000, f[-1])

    def testCorrectDeltaFrequency(self):
        t, y, f, c = self.tyfc
        self.assertEqual(100, f[1]-f[0])

    def testCorrectValueAt1000(self):
        t, y, f, c = self.tyfc
        self.assertTrue(len(c)>10)
        value = abs(c[10])
        self.assertAlmostEqual(1, value)

    def testCorrectValueAt2000(self):
        t, y, f, c = self.tyfc
        self.assertTrue(len(c)>20)
        value = abs(c[20])
        self.assertAlmostEqual(2, value)
