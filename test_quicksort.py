# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:29:01 2021

@author: jkran
"""
#Unit test for quicksort by Joshua Kranabetter

import unittest
from ListSort import quickSort
from ListSort import partition

# basic test to see if quicksort is working
class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(quickSort([4,3,2,1], 0, 3), [1,2,3,4])


