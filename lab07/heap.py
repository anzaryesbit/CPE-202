class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.size = 0                       # empty heap

    def enqueue(self, item):
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.is_full():
            raise IndexError
        self.size += 1
        self.heap[self.size] = item
        self.perc_up(self.get_size())

    def peek(self):
        """returns max without changing the heap
        Raises IndexError if the heap is empty"""
        if self.size == 0:
            raise IndexError
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        retval = self.heap[1]
        self.heap[1] = self.heap[self.get_size()]
        self.heap[self.get_size()] = None
        self.size -= 1
        self.perc_down(1)
        return retval


    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        to_display = []
        if self.is_empty():
            return to_display
        for i in range(1, len(self.heap)):
            if self.heap[i] is not None:
                to_display.append(self.heap[i])
        return to_display


    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if self.get_capacity() < len(alist):
            self.heap = [None] * (len(alist))
        else:
            self.heap = [None] * (self.get_capacity())
        capacity = self.get_capacity() + 2
        i = len(alist) // 2
        self.size = len(alist)
        self.heap = [0] + alist[:]
        if len(self.heap) < capacity:
            self.heap += [None] * (capacity - len(self.heap))
        while (i > 0):
            self.perc_down(i)
            i -= 1


    def is_empty(self):
        """returns True if the heap is empty, False otherwise"""
        return self.get_size() == 0


    def is_full(self):
        """returns True if the heap is full, False otherwise"""
        return self.get_size() == self.get_capacity()


    def get_capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap) - 1


    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size


    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.get_size():
            if i * 2 + 1 > self.get_size():
                maxval = i * 2
            else:
                if self.heap[i*2] > self.heap[i*2 + 1]:
                    maxval = i * 2
                else:
                    maxval = i * 2 + 1
            if self.heap[i] < self.heap[maxval]:
                temp = self.heap[i]
                self.heap[i] = self.heap[maxval]
                self.heap[maxval] = temp
            i = maxval


    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heap[i] > self.heap[i//2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2


    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        for i in range(1, len(alist)):
            value = alist[i]
            j = i - 1
            while j >= 0:
                if value < alist[j]:
                    alist[j + 1] = alist[j]
                    alist[j] = value
                    j -= 1
                else:
                    break

