# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self):
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self):
        tlist = [3, 2, 1]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_04(self):
        tlist = []
        self.assertIsNone(max_list_iter(tlist))

    def test_reverse_01(self):
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_02(self):
        intlist = [1, 2, 3, 4]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [4, 3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3, 4])

    def test_reverse_03(self):
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(intlist)

    def test_reverse_04(self):
        intlist = []
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [])
        self.assertEqual(intlist, [])

    def test_reverse_mutate_01(self):
        intlist = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

    def test_reverse_mutate_02(self):
        intlist = [1, 2, 3, 4]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [4, 3, 2, 1])

    def test_reverse_mutate_03(self):
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(intlist)

    def test_reverse_mutate_04(self):
        intlist = []
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [])

if __name__ == "__main__":
        unittest.main()