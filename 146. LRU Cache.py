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

class DlinkedList:
    def __init__(self):
        self.head = DNode(0,0)
        self.tail = DNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, node):
        pos = self.head.next
        pos.prev = node
        node.next = pos
        node.prev = self.head
        self.head.next = node
    
    def removeNode(self,node):
        pre = node.prev
        pos = node.next
        pre.next = pos
        pos.prev = pre

class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # Cache starts empty and capacity is set by client
        self.hashtable = collections.defaultdict()
        self.size = capacity
        self.dlist = DlinkedList()
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashtable:
            n = self.hashtable.get(key)
            self.dlist.removeNode(n)   # keep LRU feature, put recently visited element to the head of list
            self.dlist.addNode(n)
            return n.val
        else:
            return -1
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashtable:
            n = self.hashtable.get(key)
            self.dlist.removeNode(n)
            self.dlist.addNode(n)
            n.val = value
        
        else:
            if self.size == len(self.hashtable):
                tmp = self.dlist.tail.prev
                
                self.dlist.removeNode(tmp)
                self.hashtable.pop(tmp.key)
            
            node = DNode(key,value)
            self.dlist.addNode(node)
            self.hashtable[key] = node






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
