from ListSort import feature3
import unittest


class TestSelectionSort(unittest.TestCase):
    def test_selection(self):
        self.assertEqual(feature3([4,3,2,1]), [1,2,3,4])
