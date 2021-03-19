import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import numpy as np
import matplotlib.pyplot as plt

import taylorreihe as MUT


class testSinusFunction(unittest.TestCase):
    def setUp(self):
        self.fkt = MUT.SineFunction()

    def testLatex(self):
        self.assertEqual(self.fkt.getLatex(), "$sin(x)$")

    def testEval(self):
        x = 2
        self.assertIsNotNone(self.fkt.evaluate(x))
        self.assertAlmostEqual(self.fkt.evaluate(x), np.sin(x))

    def testEvalDeriv(self):
        x = 2
        self.assertIsNotNone(self.fkt.evalDerivitive(0, x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(0, x), np.sin(x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(1, x), np.cos(x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(10, x), -np.sin(x))

    def testEvalDerivVector(self):
        x = np.linspace(0, 10)
        d = self.fkt.evalDerivitive(10, x)
        self.assertIsNotNone(d)

        np.testing.assert_array_almost_equal(d, -np.sin(x))


class testExpFunction(unittest.TestCase):
    def setUp(self):
        self.fkt = MUT.ExpFunction()

    def testLatex(self):
        self.assertEqual(self.fkt.getLatex(), "$e^x$")

    def testEval(self):
        x = 2
        self.assertIsNotNone(self.fkt.evaluate(x))
        self.assertAlmostEqual(self.fkt.evaluate(x), np.exp(x))

    def testEvalDeriv(self):
        x = 2
        self.assertIsNotNone(self.fkt.evaluate(x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(0, x), np.exp(x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(1, x), np.exp(x))
        self.assertAlmostEqual(self.fkt.evalDerivitive(10, x), np.exp(x))

    def testEvalDerivVector(self):
        x = np.linspace(0, 10)
        self.assertIsNotNone(self.fkt.evaluate(x))
        np.testing.assert_array_almost_equal(self.fkt.evalDerivitive(10, x), np.exp(x))


class testTaylorApproximation(unittest.TestCase):
    def setUp(self):
        fkt = MUT.SineFunction()

        N = 3
        x0 = 32
        self.taylor = MUT.TaylorApproximation(fkt, N, x0)

    def testCoefficients(self):
        ta = self.taylor
        expected = [-0.13903722675108504, -0.2757133406208453, 0.8342233605065102, 0.5514266812416906]
        C = ta.calcTaylorCoefficients()
        self.assertIsNotNone(C)

        np.testing.assert_array_almost_equal(C, expected)

    def testGetTaylorPolynom1(self):
        poly = self.taylor.getTaylorPolynom()
        self.assertIsInstance(poly, np.poly1d)

    def testGetTaylorPolynom2(self):
        poly = self.taylor.getTaylorPolynom()
        self.assertIsNotNone(poly)

        self.assertEqual(poly[0], 0.5514266812416906)
        self.assertEqual(len(poly), 3)

    def testEvaluate(self):
        ta = self.taylor
        self.assertEqual(ta.evaluate(30), -1.1075755882460308)

    def testGetLatex(self):
        expected = r'$0.551(x-x_0)^{0} + 0.834(x-x_0)^{1} - 0.276(x-x_0)^{2} - 0.139(x-x_0)^{3}$'
        self.assertEqual(self.taylor.getLatex(), expected)

class testPlotFunction(unittest.TestCase):
    def setUp(self):
        self.fig = plt.figure()
        ax = self.fig.gca()
        x0 = 3
        N = 4
        fktname = 'sin(x)'
        MUT.plotFunction(ax, x0, N, fktname)
        self.ax = ax

    def testNumberOfPlotlines(self):
        ax = self.ax
        self.assertEqual(len(ax.lines), 3)

    def testLabels(self):
        lbl = [line.get_label() for line in self.ax.lines]

        self.assertIn('$sin(x)$', lbl)
        self.assertIn(r'$0.141(x-x_0)^{0} - 0.990(x-x_0)^{1} - 0.071(x-x_0)^{2} + 0.165(x-x_0)^{3} + 0.006(x-x_0)^{4}$', lbl)
        self.assertIn('$x_0$', lbl)

    def testXRange(self):
        ax = self.ax
        self.assertGreater(len(ax.lines), 1)
        xdata = ax.lines[0]._x
        self.assertEqual(xdata.min(), -10)
        self.assertEqual(xdata.max(), 10)
        self.assertEqual(len(xdata), 400)

    def testYValues(self):
        self.assertGreater(len(self.ax.lines), 1)

        lbl = [line.get_label() for line in self.ax.lines]
        for idx, l in enumerate(lbl):
            if '(x-x_0)' in l:
                break

        ydata = self.ax.lines[idx]._y
        ydata = ydata[:4]
        expected = [-193.47718113, -191.83317561, -190.19200553, -188.55377591]
        np.testing.assert_array_almost_equal(ydata, expected)

class testPlotFunctionExp(unittest.TestCase):
    def setUp(self):
        self.fig = plt.figure()
        ax = self.fig.gca()
        x0 = 3
        N = 4
        fktname = 'exp(x)'
        MUT.plotFunction(ax, x0, N, fktname)
        self.ax = ax

    def testYValues(self):
        self.assertGreater(len(self.ax.lines), 1)

        lbl = [line.get_label() for line in self.ax.lines]
        for idx, l in enumerate(lbl):
            if '(x-x_0)' in l:
                break

        ydata = self.ax.lines[idx]._y
        ydata = ydata[:4]
        expected = [18004.17316 , 17710.335705, 17420.126743, 17133.516109]
        np.testing.assert_array_almost_equal(ydata, expected)


class testPlotFunctionGeneral(unittest.TestCase):
    def testUnknownFunction(self):
        with self.assertRaises(ValueError):
            self.fig = plt.figure()
            ax = self.fig.gca()
            x0 = 3
            N = 4
            fktname = 'gibtesnicht(x)'
            MUT.plotFunction(ax, x0, N, fktname)

