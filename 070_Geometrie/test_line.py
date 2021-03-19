import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import numpy as np

from line import Line

class testLineObject(unittest.TestCase):
    def testLength(self):
        p1xy = (10, 5)
        p2xy = (13, 9)

        line = Line(p1xy, p2xy)
        self.assertAlmostEqual(line.length(), 5)

    def testAngle1(self):
        import math
        for angle in [0, 45, 90, 135, 180, 225, 270]:
            dx = 100*math.cos(angle / 180 * math.pi)
            dy = 100*math.sin(angle / 180 * math.pi)
            p1xy = [100, 200]
            p2xy = [p1xy[0]+dx, p1xy[1]+dy]

            line = Line(p1xy, p2xy)
            self.assertAlmostEqual(line.angle(), angle)


    def testRotate1(self):
        L1 = Line((20, 30), (20, 10))
        L2 = L1.rotate(33)

        self.assertAlmostEqual(L1.angle(), 270)
        self.assertAlmostEqual(L2.angle(), 303)

    def testRotate2(self):
        L1 = Line((20, 30), (0, 10))
        L2 = L1.rotate(-226)

        self.assertAlmostEqual(L1.angle(), 225)
        self.assertAlmostEqual(L2.angle(), 359)

    def testRotate3(self):
        L1 = Line((-10, -10), (10, 10))
        L2 = L1.rotate(45)

        p1, p2 = L2.getEdges()
        t = np.array( [p1, p2] )
        ex = np.array( [[0, -np.sqrt(2)*10], [0, np.sqrt(2)*10]] )

        np.testing.assert_array_almost_equal(t, ex)
