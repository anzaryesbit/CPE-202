from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:

    def __init__(self):  # Returns empty BST
        self.root = None

    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None

    def search(self, key):  # returns True if key is in a node of the tree, else False
        cur = self.root
        return self.search_helper(key, cur)


    def insert(self, key, data=None):  # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            inserted = False
            cur = self.root
            while not inserted:
                if key < cur.key:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = TreeNode(key, data)
                        inserted = True
                elif key > cur.key:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = TreeNode(key, data)
                        inserted = True
                else:
                    cur.data = data
                    inserted = True

    def find_min(self):  # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.key, cur.data

    def find_max(self):  # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.key, cur.data

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        cur = self.root
        return self.tree_height_helper(cur)

    def inorder_list(self):  # return Python list of BST keys representing in-order traversal of BST
        io_list = []
        self.inorder_list_helper(self.root, io_list)
        return io_list

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        po_list = []
        self.preorder_list_helper(self.root, po_list)
        return po_list

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        cur = self.root
        pylist = []
        self.levelOrder(cur, q, pylist)
        return pylist

    def tree_height_helper(self, node):
        if node is None:
            return -1
        else:
            return max(self.tree_height_helper(node.left), self.tree_height_helper(node.right)) + 1

    def inorder_list_helper(self, node, pylist):
        if node is not None:
            self.inorder_list_helper(node.left, pylist)
            pylist.append(node.key)
            self.inorder_list_helper(node.right, pylist)

    def preorder_list_helper(self, node, pylist):
        if node is not None:
            pylist.append(node.key)
            self.preorder_list_helper(node.left, pylist)
            self.preorder_list_helper(node.right, pylist)

    def levelOrder(self, root, q, pylist):
        h = self.tree_height()
        for i in range(1, h + 2):
            self.printGivenLevel(root, i, q)
            while not q.is_empty():
                pylist.append(q.dequeue())
        return pylist

    def printGivenLevel(self, root, level, q):
        if root is None:
            return
        if level == 1:
            q.enqueue(root.key)
        elif level > 1:
            self.printGivenLevel(root.left, level - 1, q)
            self.printGivenLevel(root.right, level - 1, q)

    def search_helper(self, key, node):
        if node is None:
            return False
        elif node.key == key:
            return True
        elif node.key > key:
            node = node.left
            return self.search_helper(key, node)
        elif node.key < key:
            node = node.right
            return self.search_helper(key, node)

