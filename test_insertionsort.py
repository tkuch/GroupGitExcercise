# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:05:26 2021

@author: tkuch
"""
#Unit test for insertion sort by Tasha Kucher

import unittest
from ListSort import feature5

# basic test to see if insertion sort is working
class Test_TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(feature5([4,3,2,1]), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()