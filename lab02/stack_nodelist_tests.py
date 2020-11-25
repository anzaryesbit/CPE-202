import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_stack_empty(self):
        stack1 = Stack()
        self.assertTrue(stack1.is_empty())

        init_stack2 = Node(1, None)
        stack2 = Stack(init_stack2)
        self.assertFalse(stack2.is_empty())

    def test_stack_push(self):
        init_stack = Node(2, Node(1, None))
        stack1 = Stack(init_stack)
        stack1.push(3)
        stack2 = Stack(Node(3, Node(2, Node(1, None))))
        self.assertEqual(stack1, stack2)

    def test_stack_pop(self):
        init_stack1 = Node(2, Node(1, None))
        stack1 = Stack(init_stack1)
        self.assertEqual(stack1.pop(), 2)

        stack2 = Stack()
        with self.assertRaises(IndexError):
            stack2.pop()

    def test_stack_peek(self):
        init_stack1 = Node(2, Node(1, None))
        stack1 = Stack(init_stack1)
        self.assertEqual(stack1.peek(), 2)

        stack2 = Stack()
        with self.assertRaises(IndexError):
            stack2.peek()

    def test_stack_size(self):
        init_stack1 = Node(2, Node(1, None))
        stack1 = Stack(init_stack1)
        self.assertEqual(stack1.size(), 2)

if __name__ == '__main__': 
    unittest.main()
