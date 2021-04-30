# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:18:53 2020

@author: torsten
"""

import sys
import os

sys.path.insert(0, os.path.split(__file__)[0])

from fizzbuzz import *

import unittest


class Test(unittest.TestCase):
    def test_single(self):
        self.assertEqual(fizzbuzzNumber(1), '1')
        self.assertEqual(fizzbuzzNumber(98), '98')
        self.assertEqual(fizzbuzzNumber(3), 'Fizz')
        self.assertEqual(fizzbuzzNumber(5), 'Buzz')
        self.assertEqual(fizzbuzzNumber(30), 'FizzBuzz')

    def test_all(self):
        result = run()
        expected = ("1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz\n"
                    "11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz\n"
                    "Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz\n"
                    "31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz\n"
                    "41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz\n"
                    "Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz\n"
                    "61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz\n"
                    "71, Fizz, 73, 74, FizzBuzz, 76, 77, Fizz, 79, Buzz\n"
                    "Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, FizzBuzz\n"
                    "91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz\n")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
