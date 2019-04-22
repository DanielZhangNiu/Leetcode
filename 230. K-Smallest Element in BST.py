
"""
    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
    
    Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
    
    Example 1:
    
    Input: root = [3,1,4,null,2], k = 1
    3
   / \
  1   4
   \
    2
    Output: 1
    Example 2:
    
    Input: root = [5,3,6,2,4,null,null,1], k = 3
     5
    / \
   3   6
  / \
 2   4
/
1
    Output: 3
    Follow up:
    What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def kthSmallest(root, k):
    """
        :type root: TreeNode
        :type k: int
        :rtype: int
        
        self.res = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return self.res[k-1]
    """
    if not root: return None
    p = root
    stack = []
    while p or stack:
        if p:
            stack.append(p.val)
            p = p.left
        else:
            node = stack.pop()
            k-=1
            if k == 0: return node.val
            p = node.right
    return None




