# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.capacity

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def _get_hash(self, key):
        pass

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        key_hash = self._hash(key)
        key_value = [key, value]

        if self.storage[key_hash] is None:
            self.storage[key_hash] = list([key_value])
            return True
        else:
            for pair in self.storage[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.storage[key_hash].append(key_value)
            return True

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)

        if self.storage[hashed_key] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.storage[hashed_key][i][0] == key:
                self.storage[hashed_key].pop(i)
                return True

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_hash = self._hash(key)
        if self.storage[key_hash] is not None:
            for pair in self.storage[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity * 2

        for i in range(self.length):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

        print('RESIZE ME ')


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("INSERTED COMPLETE")

    print("RETRIEVING VALUES=>")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    print('---before resize()----')
    ht.resize()
    print('---after resize()----')
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("/n")
    print("n/END OF PROGRAM")
