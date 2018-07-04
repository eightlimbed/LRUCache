### LRU Cache Implementation

LRU Cache implementation using a hash map and a doubly-linked list.

The hash map gives us O(1) times for get() and set().

We also want O(1) for inserting and deleting objects from the cache. Doubly
linked lists allow us to achieve that, assuming we have references to nodes the
'tail' and 'head' nodes.

So we can get O(1) for get(), set(), insert(), and delete() using a combination
of these two data structures.

Thanks to [Programmer Mitch](https://www.youtube.com/watch?v=R0GTqg3pJKg) for
the helpful video.
