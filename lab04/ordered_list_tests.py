import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_more(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(10)
        t_list.add(30)
        t_list.add(15)
        t_list.add(40)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(40), 4)
        self.assertEqual(t_list.size(), 5)
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.python_list(), [15, 20, 30, 40])
        self.assertEqual(t_list.size(), 4)

    def test_thorough(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(10)
        t_list.add(30)
        t_list.add(15)
        t_list.add(40)
        self.assertFalse(t_list.remove(25))
        self.assertTrue(t_list.remove(30))
        self.assertTrue(t_list.remove(40))
        self.assertEqual(t_list.index(18), None)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        t_list.add(25)
        t_list.add(40)
        t_list.add(30)
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.pop(4), 40)
        self.assertEqual(t_list.pop(2), 25)
        self.assertEqual(t_list.python_list_reversed_helper([1, 2, 3]), [3, 2, 1])


if __name__ == '__main__': 
    unittest.main()
