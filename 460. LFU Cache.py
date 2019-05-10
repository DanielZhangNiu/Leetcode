"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

"""
We actually maintain most of the structure of LRU cache implemented before, except we add one primary hashtable which called freqtable here, {freq:{Dlinkedlist node1,Dlinkedlist node2 .... }}
in each key of this freqtable, we keep the LRU sequnce, recently used element put in head, pop the tail one when capacity is full. Additionally, use a min_freq global variable to keep track minimum frequency, also helps us to locate the right key val in freqlist to manipulcate remove.
    
    
Consequence ==> The tail of the DLinkedList with self.min_freq is the least
recently used one, pop it...
"""
import collections
class Node:
    def __init__(self,key,value):
        self.val = value
        self.key = key
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addNode(self,node):
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

class LFUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.nodetable =dict()
        self.freqtable = collections.defaultdict(DLinkedList)
        self.min_freq = 0

    def get(self, key):
        """
        Through checking self.nodetable[key], we can get the node in O(1) time.
        Just performs self.updatelist tp maintain the dlist structure, then we can return the value of node.
        
        :type key: int
        :rtype: int
        """
        if key in self.nodetable:
            node = self.nodetable.get(key)
            self.update(node)
            return node.val
        else:
            return -1


    def put(self,key,value):
        """
        If `key` already exists in self.nodetable,perform updatelist, put increase the frequency of this key and
        updating the node.val to new value.
            
        Otherwise, the following logic will be performed
            
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self.nodetable
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
            
        (*) How to pop the least frequently used item? Two facts:
            
        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored in a DLinkedList, with
        recently used order (Always append at head)
            
        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
        recently used one, pop it...
            
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodetable:
            node = self.nodetable.get(key)
            self.update(node)
            node.val = value
        else:

            if self.capacity == 0:
                return
            if self.capacity == len(self.nodetable):
                old_node = self.freqtable[min_freq].tail.prev
                self.nodetable.pop(old_node)
                self.freqtable[min_freq].pop(old_node

            new_node = Node(key,value)
            self.nodetable[key] = new_node
            self.freqtable[1].addNode(new_node)
            self.min_freq = 1



    def update(self,node):
                                             
        """
        This is a helper function that used in the following two cases:
                                                 
        1. when `get(key)` is called; and
        2. when `put(key, value)` is called and the key exists.
                                                 
        The common point of these two cases is that:
                                                 
        1. no new node comes in, and
        2. the node is visited one more times -> node.freq changed ->thus the place of this node will change
                                                 
        The logic of this function is:
                                                 
        1. remove the node from the old DLinkedList (with freq `f`)
        2. append the node to new DLinkedList (with freq `f+1`)
        3. if old DlinkedList has size 0 and self._minfreq is `f`, update self._minfreq to `f+1`
                                                 
        All of the above opeartions took O(1) time.
        """
        freq = node.freq
        self.freqtable[freq].removeNode(node)

        if self.freqtable[freq].head.next == self.freqtable[freq].tail and self.min_freq == freq:
            self.min_freq += 1

        node.freq += 1
        freq = node.freq
        self.freqtable[freq].addNode(node)





