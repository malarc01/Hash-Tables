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
        return hash(key)

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

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # make an index from the hash
        index = self._hash_mod(key)

        # create link node using key/value
        linked_pair = LinkedPair(key, value)

        # each index has a link list
        # travel down that link list

        # set current to that index
        current_index = self.storage[index]

        # if no link list at index
        if current_index == None:
            # put the new node there & return
            self.storage[index] = linked_pair
            return

        # set previous to None for looping
        previous = None
        # loop through nodes that exist
        while current_index != None:
            # if we find a key match
            if current_index.key == key:
                # overwrite value & return
                current_index.value = value
                return
            # if no match, continue down list
            previous = current_index
            current_index = current_index.next

        # if node not found in list, add it to end
        previous.next = linked_pair

        # if self.storage[index] is not None:

        # print('COLLISION @ incoming key, value ', key, value)
        # set the next value to the next Linked Pair
        # print('b next=>', self.storage[index].next)
        # self.storage[index].next = self.storage[index]
        # print('current key=>', self.storage[index].key)
        # print('current value=>', self.storage[index].value)
        # print('a current next=>', self.storage[index].next)
        # self.storage[index] = LinkedPair(key, value)
        # if slot is empty just insert it as a Linked Pair object
        # else:
        # self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # make an index from the hash of the key
        index = self._hash_mod(key)
        # save it as current, make previous
        previous = None
        current_index = self.storage[index]

        # remove that node
        while current_index is not None:
            # check if keys match
            if current_index.key == key:
                # if head of list, set next value
                if previous is None:
                    self.storage[index] = current_index.next
                # if not head of list, connect nodes
                else:
                    previous.next = current_index.next
                return

            # iterate through by advancing pointers
            previous = current_index
            current_index = current_index.next

        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # make pointer
        current_index = self.storage[index]

        # iterate through the list
        while current_index != None:
            # if the keys match
            if current_index.key == key:
                # return value
                return current_index.value
            # if no match, increment pointer
            else:
                current_index = current_index.next

        return

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        double_hashmap = HashTable(self.capacity * 2)

        for item in range(self.capacity):

            if self.storage[item] is not None:

                current = self.storage[item]
                while current is not None:

                    double_hashmap.insert(current.key, current.value)

                    current = current.next

        # set old table to new table
        self.capacity = double_hashmap.capacity
        self.storage = double_hashmap.storage

        return


if __name__ == "__main__":
    ht = HashTable(8)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    print("----HashTable(8)----")

    # Test storing beyond capacity
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    # ht.insert("key-6", "val-6")
    # ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("key-0"))
    print(ht.retrieve("key-1"))
    print(ht.retrieve("key-2"))
    print(ht.retrieve("key-3"))
    print(ht.retrieve("key-4"))
    print(ht.retrieve("key-5"))

    # ht.remove("key-9")
    # ht.remove("key-8")
    # ht.remove("key-7")
    # ht.remove("key-6")
    # ht.remove("key-5")
    # ht.remove("key-4")
    # ht.remove("key-3")
    # ht.remove("key-2")
    # ht.remove("key-1")

    # ht.resize()



    print("---END---")
