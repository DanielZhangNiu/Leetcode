"""
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
    
    Example:
    
    Input:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    Output: 1->1->2->3->4->4->5->6

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

