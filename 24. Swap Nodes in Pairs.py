"""
    Given a linked list, swap every two adjacent nodes and return its head.
    
    You may not modify the values in the list's nodes, only nodes itself may be changed.
    
    
    
    Example:
    
    Given 1->2->3->4, you should return the list as 2->1->4->3.
   

"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#       self.val = x
#       self.next = None


def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
    dummy = cur = ListNode(0)
    h = []
    # build minheap from every first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(h,(node.val,i,node))
        
    while h:
        val,idx,newnode = heapq.heappop(h)
        cur.next = newnode
        if newnode.next:
            heapq.heappush(h,(newnode.next.val,idx,newnode.next))
        cur = cur.next
    return dummy.next

