
"""
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    
    You should preserve the original relative order of the nodes in each of the two partitions.
    
    Example:
    
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5

"""
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    def partition(head: ListNode, x: int) -> ListNode:
        ls = dummyls = ListNode(0)
        gs = dummygs = ListNode(0)
        
        while head:
            if head.val < x:
                ls.next = ListNode(head.val)
                ls = ls.next
            else:
                gs.next = ListNode(head.val)
                gs = gs.next
            head = head.next
        
        ls.next = dummygs.next
        return dummyls.next

