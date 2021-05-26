
#Unit test for mergeSortby J

import unittest
from ListSort import feature4

class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(feature4([3,4,2,1]), [1,2,3,4])