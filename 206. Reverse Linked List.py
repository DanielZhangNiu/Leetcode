"""
    Reverse a singly linked list.
    
    Example:
    
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
    Follow up:
    
    A linked list can be reversed either iteratively or recursively. Could you implement both?
    

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    """
        :type head: ListNode
        :rtype: ListNode
        
        tmp = None
        dummy = head
        while dummy:
            cur = dummy
            dummy = dummy.next
            cur.next = tmp
            tmp = cur
        return tmp
        """
            
    return _reverse(head,None)
        
def _reverse(node, prev):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return _reverse(n, node)
