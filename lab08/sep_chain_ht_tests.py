import unittest
from sep_chain_ht import *


class TestList(unittest.TestCase):

    def test_insert1(self):
        hash1 = MyHashTable()
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.size(), 2)
        with self.assertRaises(ValueError):
            hash1.insert(-5, "c")

    def test_insert2(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(11, "b")
        self.assertListEqual(hash1.hash_table, [[], [(11, "b")], [], [], []])

    def test_insert3(self):
        hash1 = MyHashTable(2)
        hash1.insert(2, "a")
        hash1.insert(1, "b")
        self.assertListEqual(hash1.hash_table, [[(2, "a")], [(1, "b")]])
        hash1.insert(10, "b")
        self.assertEqual(hash1.size(), 5)
        self.assertListEqual(hash1.hash_table, [[(10, "b")], [(1, "b")], [(2, "a")], [], []])

    def test_insert4(self):
        hash1 = MyHashTable()
        hash1.insert(1, "a")
        hash1.insert(12, "b")
        self.assertListEqual(hash1.hash_table, [[], [(1, "a"), (12, "b")], [], [], [], [], [], [], [], [], []])

    def test_insert5(self):
        hash1 = MyHashTable(2)
        hash1.insert(1, "a")
        hash1.insert(3, "b")
        self.assertListEqual(hash1.hash_table, [[], [(1, "a"), (3, "b")]])
        hash1.insert(2, "c")
        self.assertEqual(hash1.size(), 5)
        self.assertListEqual(hash1.hash_table, [[], [(1, "a")], [(2, "c")], [(3, "b")], []])

    def test_get1(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.get_item(3), 'b')
        self.assertEqual(hash1.get_item(11), 'a')

    def test_get2(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        with self.assertRaises(LookupError):
            hash1.get_item(6)

    def test_get3(self):
        hash1 = MyHashTable()
        with self.assertRaises(LookupError):
            hash1.get_item(1)

    def test_remove1(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        self.assertEqual(hash1.remove(11), (11, 'a'))
        self.assertEqual(hash1.size(), 0)

    def test_remove2(self):
        hash1 = MyHashTable()
        hash1.insert(11, "a")
        hash1.insert(1, "b")
        hash1.insert(12, "c")
        self.assertEqual(hash1.remove(12), (12, "c"))
        self.assertEqual(hash1.size(), 2)
        self.assertEqual(hash1.hash_table, [[(11, "a")], [(1, "b")], [], [], [], [], [], [], [], [], []])

    def test_remove3(self):
        hash1 = MyHashTable()
        with self.assertRaises(LookupError):
            hash1.remove(1)

    def test_load_factor1(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.load_factor(), 1.4)

    def test_collisions2(self):
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertListEqual(hash1.hash_table,
                             [[(5, "f")], [(11, "a"), (1, "g")], [(2, "h")], [(3, "b"), (8, "d")], [(4, 'e')]])
        self.assertEqual(hash1.collisions(), 2)


if __name__ == '__main__':
    unittest.main()
