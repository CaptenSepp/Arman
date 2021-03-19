# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:18:53 2020

@author: thorsten
"""

import sys
import os

sys.path.insert(0, os.path.split(__file__)[0])

from lottozahlen import *
from unittest.mock import patch
from unittest import TestCase

class Test(TestCase):
    def test_draw_is_7(self):
        self.assertTrue(len(get_draw()) == 7)

    def test_draw_is_unique(self):
        self.assertTrue(len(get_draw()) == len(set(get_draw())))

    def test_draw_is_7(self):
        self.assertTrue(len(get_draw()) == 7)

    is_unique = [1, 2, 3, 4, 5, 6, 7]

    @patch('lottozahlen.get_input', return_value=1, side_effect=is_unique)
    def test_user_input_is_7(self, input):
        result = user_input()
        expect = 7
        self.assertTrue(len(result) == expect)

    not_unique = [1, 2, 3, 4, 5, 6, 1, 1, 7]

    @patch('lottozahlen.get_input', return_value=1, side_effect=not_unique)
    def test_user_input_is_7_unique(self, input):
        result = user_input()
        expect = 7
        self.assertTrue(len(result) == expect)

    @patch('lottozahlen.get_input', return_value=1, side_effect=not_unique)
    def test_user_input_is_not_unique(self, input):
        user = user_input()
        expect = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(user, expect)

    def test_lottozahlen_validate_1(self):
        self.assertEqual(validate_input(1), 1)

    def test_lottozahlen_validate_2(self):
        self.assertEqual(validate_input(49), 49)

    def test_lottozahlen_validate_3(self):
        self.assertEqual(validate_input(50), False)

    def test_lottozahlen_validate_4(self):
        self.assertEqual(validate_input(0), False)

    def test_lottozahlen_validate_5(self):
        self.assertEqual(validate_input('a'), False)

    def test_lottozahlen_validate_6(self):
        self.assertEqual(validate_input(''), False)

    def test_lottozahlen_check_numbers(self):
        expect = [1, 2, 3, 4, 5, 6, 7]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(check_numbers(expect, result), result)


if __name__ == '__main__':
    main()
