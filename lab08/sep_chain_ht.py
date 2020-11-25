
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, value):
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError
        self.num_items += 1
        hash_value = key % self.table_size
        if self.hash_table[hash_value] != []:
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == key:
                    self.num_items -= 1
                    self.hash_table[hash_value][i] = (key, value)
                    return None
            if self.load_factor() >= 1.5:
                self.rehash()
            self.num_collisions += 1
            hash_value = key % self.table_size
            self.hash_table[hash_value].append((key, value))
        else:
            if self.load_factor() >= 1.5:
                self.rehash()
            hash_value = key % self.table_size
            self.hash_table[hash_value].append((key, value))

    def rehash(self):
        temp_size = self.table_size
        temp = self.hash_table
        new_size = temp_size * 2 + 1
        self.table_size = new_size
        self.hash_table = [[] for _ in range(self.table_size)]
        for value in temp:
            if value != []:
                for char in value:
                    self.insert(char[0], char[1])

    def get_item(self, key):
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        hash_value = key % self.table_size
        for char in self.hash_table[hash_value]:
            if char[0] == key:
                return char[1]
        raise LookupError


    def remove(self, key):
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        hash_value = key % self.table_size
        for i in range(len(self.hash_table[hash_value])):
            char = self.hash_table[hash_value][i]
            if char[0] == key:
                self.num_items -= 1
                to_remove = self.hash_table[hash_value].pop(i)
                return to_remove
        raise LookupError

    def load_factor(self):
        """Returns the current load factor of the hash table"""
        return self.num_items/self.table_size

    def size(self):
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self):
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions

