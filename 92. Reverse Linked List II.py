
"""
    Reverse a linked list from position m to n. Do it in one-pass.
    
    Note: 1 ≤ m ≤ n ≤ length of list.
    
    Example:
    
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

"""
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    def reverseBetween(head, m, n)::
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next  #2
        for i in range(n-m+1):
            this = cur
            cur = cur.next
            this.next = reverse
            reverse = this
        
        pre.next.next = cur #2 next is 5
        pre.next = reverse # 1 next is 4
        return dummy.next

