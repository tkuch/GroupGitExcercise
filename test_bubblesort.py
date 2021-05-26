# -*- coding: utf-8 -*-
"""
Created on Mon May 24 03:25:01 2021

@author: lukesparg
"""
#Unit test for bubblesort by Luke Sparg

import unittest
from ListSort import bubbleSort
from ListSort import partition

# basic test to see if quicksort is working
class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(bubbleSort([4,3,2,1]), [1,2,3,4])


