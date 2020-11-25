import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self):
        stack1 = Stack(5)
        self.assertTrue(stack1.is_empty())

        stack2 = Stack(2, [1])
        self.assertFalse(stack2.is_empty())

    def test_is_full(self):
        stack1 = Stack(2, [1, 2])
        self.assertTrue(stack1.is_full())

        stack2 = Stack(2, [1])
        self.assertFalse(stack2.is_full())

    def test_push(self):
        stack1 = Stack(3, [1, 2])
        stack1.push(4)
        self.assertEqual(stack1.items, [1, 2, 4])

        stack2 = Stack(1, [1])
        with self.assertRaises(IndexError):
            stack2.push(2)

    def test_pop(self):
        stack1 = Stack(2, [1, 2])
        self.assertEqual(stack1.pop(), 2)

        stack2 = Stack(5)
        with self.assertRaises(IndexError):
            stack2.pop()

    def test_peek(self):
        stack1 = Stack(3, [1, 2])
        self.assertEqual(stack1.peek(), 2)

        stack2 = Stack(5)
        with self.assertRaises(IndexError):
            stack2.peek()

if __name__ == '__main__': 
    unittest.main()
