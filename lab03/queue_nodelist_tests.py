import unittest

from queue_nodelist import *

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue()
        q.is_empty()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue()
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.front, None)
        self.assertEqual(q1.rear, None)

    def test_examples(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        self.assertFalse(q1.is_empty())
        self.assertEqual(q1.size(), 3)
        self.assertEqual(q1.dequeue(),1)
        q2 = Queue()
        q2.enqueue(2)
        q2.enqueue(3)
        self.assertEqual(q1, q2)

    def test_more_examples(self):
        q1 = Queue()
        q1.enqueue(1)
        q1.enqueue(2)
        self.assertEqual(q1.dequeue(), 1)
        q1.enqueue(3)
        self.assertEqual(q1.__repr__(), "Queue(Node(3, None), Node(2, None))")
        self.assertEqual(q1.dequeue(), 2)

    def test_error(self):
        q1 = Queue()
        with self.assertRaises(IndexError):
            q1.dequeue()

if __name__ == '__main__': 
    unittest.main()
