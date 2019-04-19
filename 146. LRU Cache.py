"""
    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
    
    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    
    Follow up:
    Could you do both operations in O(1) time complexity?
    
    Example:
    
    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    
"""
class DNode:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity):
        """
            :type capacity: int
        """
        # Cache starts empty and capacity is set by client
        self.hashtable = collections.defaultdict()
        self.size = capacity
        self.head = DNode(0,0)
        self.tail = DNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        """
            :type key: int
            :rtype: int
        """
        if key in self.hashtable:
            n = self.hashtable.get(key)
            self.removeNode(n)   # keep LRU feature, put recently visited element to the tail of list
            self.addNode(n)
            return n.val
        else:
            return -1

    def addNode(self, node):
        pre = self.tail.prev
        pre.next = node
        node.prev = pre
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self,node):
        pre = node.prev
        pos = node.next
        pre.next = pos
        pos.prev = pre
    # Remove the given node from the doubly linked list

    def put(self, key, value):
        """
            :type key: int
            :type value: int
            :rtype: void
        """
        if key in self.hashtable:
            n = self.hashtable.get(key)
            self.hashtable.pop(n.key)
            self.removeNode(n)
                
        node = DNode(key,value)
        self.addNode(node)
        self.hashtable[key] = node
        
        if self.size < len(self.hashtable):
            tmp = self.head.next
            self.removeNode(tmp)
            self.hashtable.pop(tmp.key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
