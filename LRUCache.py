#!/usr/bin/python3

'''
LRU Cache implementation using a hash map and a doubly-linked list.

The hash map gives us O(1) times for get() and set().

We also want O(1) for inserting and deleting objects from the cache. Doubly
linked lists allow us to achieve that, assuming we have references to nodes the
'tail' and 'head' nodes.

So we can get O(1) for get(), set(), insert(), and delete() using a combination
of these two data structures.
'''

class Node:
    '''
        Blueprint for each node that makes up the doubly linked list.
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    '''
        Blueprint for the LRU Cache.
        `capacity` is the number of objects it can hold.
        `head` marks the 'coldest' (Least Recently Used) objects in the cache.
        `tail` makes the 'hottest' (Most Recently Added) objects in the cache.

        Functionality:
            get(key) - Returns the value of a key, if it exists.
            set(key, val) - Creates new Node and adds it to the cache.
            insert(node) - Inserts a Node into the list.
            remove(node) - Removes a Node from the list.
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.objects = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        # Head and Tail will point to eachother, making the list circular
        self.head.next = self.tail
        self.tail.next = self.head

    def get(self, key):
        # When we get() an object, we also need to update it's hotness. In
        # other words, move it towards the tail side of the linked list.
        if key in self.objects:
            node = self.objects[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1 # not found

    def set(self, key, val):
        # If the key already exists in the cache, remove it first, then add it
        # again to update it's hotness.
        if key in self.objects:
            del self.objects[key]

        # Create new node and insert it at the tail (most recently used)
        node = Node(key, val)
        self.insert(node)
        self.objects[key] = node

        # Check the capacity. If over capacity, remove the LRU node from the
        # list and the hashmap
        if len(self.objects) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.objects[lru_node.key]


    def insert(self, node):
        # We will insert new nodes at the tail
        prev = self.tail.prev
        if prev:
            prev.next = node
        else:
            self.tail.prev = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail

    def remove(self, node):
        # Remove from the head (least recently used)
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        next.prev = prev

    def print(self):
        # Prints all objects in the cache (for testing, mainly)
        for key, node in self.objects.items():
            print('{}: {}'.format(key, node.val))

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.print()
    print(cache.get(1))
    cache.set(3, 3)
    cache.print()
