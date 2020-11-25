class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item, next=None, prev=None):
        self.item = item  # item held by Node
        self.next = next  # reference to next Node
        self.prev = prev  # reference to previous Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self, sentinel=None):
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        """Returns back True if OrderedList is empty"""
        return self.sentinel.item is None

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        current = self.sentinel
        previous = None
        stop = False
        temp = Node(item)
        if self.is_empty():
            self.sentinel = temp
            return None
        while current is not None and not stop:
            if current.item > item:
                stop = True
            elif current.item == item:
                stop = True
            else:
                previous = current
                current = current.next
        if previous is not None and current is not None:
            temp.prev = previous
            temp.next = current
            previous.next = temp
            current.prev = temp
        elif previous is not None and current is None:
            temp.prev = previous
            previous.next = temp

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        current = self.sentinel
        if not self.search(item):
            return False
        if item == current.item and len(self.python_list()) == 1:
            self.sentinel = Node(None)
            return True
        if self.index(item) == 0:
            current = current.next
            current.prev = None
            self.sentinel = current
            return True
        elif self.index(item) == self.size() - 1:
            while current is not None:
                previous = current
                current = current.next
            temp = previous
            previous = temp.prev
            previous.next = None
            return True
        else:
            while current.item != item:
                current = current.next
            left = current.prev
            right = current.next
            left.next = right
            right.prev = left
            return True

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        current = self.sentinel
        if not self.search(item):
            return None
        return self.index_helper(item, current)

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        current = self.sentinel
        previous = None
        if index < 0 or index >= self.size():
            raise IndexError
        if index == 0 and len(self.python_list()) == 1:
            to_return = current.item
            self.sentinel = Node(None)
            return to_return
        if index == 0:
            to_return = current.item
            current = current.next
            current.prev = None
            self.sentinel = current
            return to_return
        elif index == self.size()-1:
            while current is not None:
                previous = current
                current = current.next
            temp = previous
            previous = temp.prev
            current = temp
            to_return = current.item
            previous.next = None
            return to_return
        else:
            for i in range(0, index):
                current = current.next
            to_remove = current.item
            left = current.prev
            right = current.next
            left.next = right
            right.prev = left
            return to_remove

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""
        current = self.sentinel
        return self.search_helper(item, current)

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        current = self.sentinel
        python_list = []
        while current is not None:
            python_list.append(current.item)
            current = current.next
        return python_list

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        python_list = self.python_list()
        return self.python_list_reversed_helper(python_list)

    def size(self):
        """Returns number of items in the OrderedList. O(n) is OK"""
        current = self.sentinel
        return self.size_helper(current)

    def python_list_reversed_helper(self, list_input):
        length = len(list_input)
        if length <= 1:
            return list_input
        return list_input[length - 1:] + self.python_list_reversed_helper(list_input[:length - 1])

    def size_helper(self, node):
        if node is None:
            return 0
        return 1 + self.size_helper(node.next)

    def index_helper(self, item, node):
        if item == node.item:
            return 0
        return 1 + self.index_helper(item, node.next)

    def search_helper(self, item, node):
        if node is None:
            return False
        if node.item == item:
            return True
        return self.search_helper(item, node.next)
