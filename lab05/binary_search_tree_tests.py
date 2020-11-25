import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_complex(self):
        bst = BinarySearchTree()
        bst.insert(25)
        bst.insert(15)
        bst.insert(10)
        bst.insert(22)
        bst.insert(4)
        bst.insert(12)
        bst.insert(18)
        bst.insert(24)
        bst.insert(50)
        bst.insert(35)
        bst.insert(31)
        bst.insert(44)
        bst.insert(70)
        bst.insert(66)
        bst.insert(90)
        self.assertEqual(bst.inorder_list(), [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90])
        self.assertEqual(bst.preorder_list(), [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90])
        self.assertEqual(bst.level_order_list(), [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90])
        self.assertEqual(bst.find_max(), (90, None))
        self.assertEqual(bst.find_min(), (4, None))
        bst.insert(90, 'hi')
        self.assertEqual(bst.find_max(), (90, 'hi'))
        self.assertTrue(bst.search(50))
        self.assertFalse(bst.search(51))
        self.assertEqual(bst.tree_height(), 3)

    def test_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.tree_height(), None)


    def test_levelorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(16)
        bst.insert(25)
        bst.insert(6)
        bst.insert(17)
        bst.insert(0)
        bst.insert(7)
        bst.insert(29)
        bst.insert(21)
        bst.insert(51)
        bst.insert(28)
        bst.insert(46)
        self.assertEqual(bst.level_order_list(), [20, 16, 25, 6, 17, 21, 29, 0, 7, 28, 51, 46])


if __name__ == '__main__': 
    unittest.main()
