# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:21:22 2020

@author: torsten
"""

import tictactoe as DUT

import unittest
from unittest.mock import MagicMock
from unittest.mock import call


def Any(cls):
    class Any(cls):
        def __eq__(self, other):
            return True

    return Any()


class testTicTacToe_Moves(unittest.TestCase):
    def test_CreateEmptyPlayground(self):
        field = DUT.createEmptyPlayground()
        self.assertEqual(field, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    
    def test_setField(self):
        field = DUT.createEmptyPlayground()
        DUT.setField(0, 1, 'o', field)
        DUT.setField(2, 2, 'x', field)
        self.assertEqual(field, [' ', ' ', ' ', 
                                 'o', ' ', ' ', 
                                 ' ', ' ', 'x'])
    def test_SetField_OutOfField(self):
        field = DUT.createEmptyPlayground()
        with self.assertRaises(IndexError) as context:
            DUT.setField(0, 10, 'o', field)

        with self.assertRaises(IndexError) as context:
            DUT.setField(2, -5, 'o', field)

        with self.assertRaises(IndexError) as context:
            DUT.setField(3, 0, 'o', field)

    def test_SetField_UnknownToken(self):
        field = DUT.createEmptyPlayground()
        with self.assertRaises(ValueError) as context:
            DUT.setField(0, 0, ' ', field)

        with self.assertRaises(ValueError) as context:
            DUT.setField(0, 0, '', field)

        with self.assertRaises(ValueError) as context:
            DUT.setField(0, 0, 'ox', field)
        with self.assertRaises(ValueError) as context:
            DUT.setField(0, 0, 'x0', field)
            
    def test_SetField_Occupied(self):
        field = DUT.createEmptyPlayground()
        result1 = DUT.setField(0, 0, 'x', field)
        result2 = DUT.setField(0, 0, 'x', field)
        result3 = DUT.setField(0, 0, 'o', field)

        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_GetField(self):
        field = DUT.createEmptyPlayground()
        DUT.setField(0, 0, 'x', field)
        DUT.setField(1, 2, 'o', field)
       
        self.assertEqual(DUT.getField(0, 0, field) , 'x')
        self.assertEqual(DUT.getField(1, 1, field) , ' ')
        self.assertEqual(DUT.getField(1, 2, field) , 'o')
    
    def test_GetField_OutOfField(self):
        field = DUT.createEmptyPlayground()
        with self.assertRaises(IndexError) as context:
            DUT.getField(5, 0, field)
    
class testTicTacToe_StateChecks(unittest.TestCase):
    def setMany(self, tokens, field):
        for j in range(3):
            for i in range(3):
                token = tokens[i][j]
                if token in "xo":
                    DUT.setField(j, i, token, field)

    def testUnentschieden(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'oxo',
                      'oxo'], field)

        self.assertTrue(DUT.unentschieden(field))

    def testNichtUnentschieden(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'o o',
                      'oxo'], field)

        self.assertFalse(DUT.unentschieden(field))

    def testNichtGewonnen(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'o o',
                      'oxo'], field)

        self.assertIsNone(DUT.gewinner(field))

    def testGewonnenHor1(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xxx',
                      'xoo',
                      'oxo'], field)

        self.assertEqual("x", DUT.gewinner(field))

    def testGewonnenHor2(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'ooo',
                      'oxo'], field)

        self.assertEqual("o", DUT.gewinner(field))

    def testGewonnenHor3(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'oxo',
                      'ooo'], field)

        self.assertEqual("o", DUT.gewinner(field))


    def testGewonnenVert1(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'xxo',
                      'xoo'], field)

        self.assertEqual("x", DUT.gewinner(field))

    def testGewonnenVert2(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xox',
                      'xoo',
                      'oox'], field)

        self.assertEqual("o", DUT.gewinner(field))

    def testGewonnenVert3(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xoo',
                      'xxo',
                      'oxo'], field)

        self.assertEqual("o", DUT.gewinner(field))

    def testGewonnenDiag1(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xoo',
                      'xxo',
                      'oxx'], field)

        self.assertEqual("x", DUT.gewinner(field))

    def testGewonnenDiag2(self):
        field = DUT.createEmptyPlayground()
        self.setMany(['xoo',
                      'xoo',
                      'oxx'], field)

        self.assertEqual("o", DUT.gewinner(field))


class testGui(unittest.TestCase):
    def setUp(self):
        self.window = MagicMock()
        DUT.init(self.window)

    def test_repaint(self):
        painter = MagicMock()
        window = MagicMock()
        temp = DUT.drawEmptyPlayground, DUT.getField, DUT.drawToken

        DUT.drawEmptyPlayground = MagicMock()
#        DUT.getField = MagicMock()
        DUT.init(window)
        DUT.setField(1, 0, 'x', DUT.Spielfeld)
        DUT.setField(1, 2, 'o', DUT.Spielfeld)
        DUT.drawToken = MagicMock()
        DUT.repaint(width=28, height=46, painter=painter, window=window)

#        print(DUT.drawToken.mock_calls)

        DUT.drawEmptyPlayground.assert_called_with(28, 46, painter)
        painter.setPen.assert_called_with( window.thickBlackPen )

        calls = list()
        calls = [call(' ', 4.5, 7.5, 8.1, 13.5, painter, window),
                 call(' ', 4.5, 22.5, 8.1, 13.5, painter, window),
                 call(' ', 4.5, 37.5, 8.1, 13.5, painter, window),
                 call('x', 13.5, 7.5, 8.1, 13.5, painter, window),
                 call(' ', 13.5, 22.5, 8.1, 13.5, painter, window),
                 call('o', 13.5, 37.5, 8.1, 13.5, painter, window),
                 call(' ', 22.5, 7.5, 8.1, 13.5, painter, window),
                 call(' ', 22.5, 22.5, 8.1, 13.5, painter, window),
                 call(' ', 22.5, 37.5, 8.1, 13.5, painter, window)]

        DUT.drawToken.assert_has_calls(calls, any_order=True)


        DUT.drawEmptyPlayground, DUT.getField, DUT.drawToken = temp

    def test_drawtokenX(self):
        painter = MagicMock()
        window = MagicMock()
        temp_circle = DUT.drawCircle
        temp_cross = DUT.drawCross
        DUT.drawCircle = MagicMock()
        DUT.drawCross = MagicMock()

        DUT.drawToken('x', 100, 200, 30, 20, painter, window)
        DUT.drawCross.assert_called_with(100, 200, 30, 20, Any(object))
        painter.setPen.assert_called_with( window.redPen )

        DUT.drawCircle = temp_circle
        DUT.drawCross = temp_cross

    def test_drawtokenO(self):
        painter = MagicMock()
        window = MagicMock()
        temp_circle = DUT.drawCircle
        temp_cross = DUT.drawCross
        DUT.drawCircle = MagicMock()
        DUT.drawCross = MagicMock()

        DUT.drawToken('o', 100, 200, 30, 20, painter, window)
        DUT.drawCircle.assert_called_with(100, 200, 30, 20, Any(object))
        painter.setPen.assert_called_with( window.greenPen )

        DUT.drawCircle = temp_circle
        DUT.drawCross = temp_cross

    def test_drawtokenWrongToken(self):
        painter = MagicMock()
        window = MagicMock()
        with self.assertRaises(ValueError):
            DUT.drawToken('t', 100, 200, 30, 20, painter, window)

    def test_emptyGrid1(self):
        painter = MagicMock()
        width = 28
        height = 31
        DUT.drawEmptyPlayground(width, height, painter)
        calls = list()
        calls = [
            #             x   y     x   y
            call.drawLine(0 , 0,    27,   0),
            call.drawLine(0 , 10,   27,  10),
            call.drawLine(0,  20,   27,  20),
            call.drawLine(0,  30,   27,  30),

            #             x   y     x   y
            call.drawLine(0 , 0,     0 , 30),
            call.drawLine(9 , 0,     9 , 30),
            call.drawLine(18, 0,     18, 30),
            call.drawLine(27, 0,     27, 30),
        ]

        painter.assert_has_calls(calls, any_order=True)

    def test_emptyGrid(self):
        painter = MagicMock()
        width = 300
        height = 600
        DUT.drawEmptyPlayground(width, height, painter)
        calls = list()
        calls.append( call.drawLine(0, 199, 299, 199) )
        calls = [
            call.drawLine(0, 0, 299, 0),
            call.drawLine(0, 199, 299, 199),
            call.drawLine(0, 399, 299, 399),
            call.drawLine(0, 0, 0, 599),
            call.drawLine(0, 599, 299, 599),
            call.drawLine(99, 0, 99, 599),
            call.drawLine(199, 0, 199, 599),
            call.drawLine(299, 0, 299, 599)
        ]
        painter.assert_has_calls(calls, any_order=True)

    def test_mouseClick(self):
        backup = DUT.setField
        DUT.setField = MagicMock()

        DUT.mouseclick(0, 0, 300, 600, self.window)
        DUT.setField.assert_called_with(0, 0, 'x', Any(list) )

        DUT.mouseclick(100, 50, 300, 600, self.window)
        DUT.setField.assert_called_with(1, 0, 'o', Any(list) )

        DUT.setField = backup

    def testDrawCross(self):
        painter = MagicMock()
        DUT.drawCross(15, 19, 4, 9, painter)
        expected_calls = [call.drawLine(13, 14, 17, 23),
                          call.drawLine(13, 23, 17, 14),
                          call.drawLine(17, 23, 13, 14),
                          call.drawLine(17, 14, 13, 23)]

        for c in painter.mock_calls:
            self.assertIn(c, expected_calls)

        self.assertEqual(2, len(painter.mock_calls))

    def testDrawCircle(self):
        painter = MagicMock()
        DUT.drawCircle(15, 19, 4, 9, painter)
        painter.assert_has_calls([call.drawEllipse(13, 14, 4, 9)])


if __name__ == '__main__':
    unittest.main(verbosity=2)