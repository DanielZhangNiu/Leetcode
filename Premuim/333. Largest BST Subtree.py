"""
 Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

 Note:
 A subtree must include all of its descendants.

 Example:

 Input: [10,5,15,1,8,null,7]

    10
    / \
   5  15
  / \   \
 1   8   7

 Output: 3
 Explanation: The Largest BST Subtree in this case is the highlighted one.
              The return value is the subtree's size, which is 3.
 Follow up:
 Can you figure out ways to solve it with O(n) time complexity?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
    
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0, sys.maxsize, -sys.maxsize
            if not node.left and not node.right:
                self.res = max(self.res, 1)
                return 1, node.val, node.val
        
            lsize, lmin, lmax = dfs(node.left)
            rsize, rmin, rmax = dfs(node.right)
            
            if lmax < node.val < rmin:
                size = lsize + 1 + rsize
                self.res = max(self.res, size)
                return size, min(lmin, node.val), max(rmax, node.val)
            
            return 0, -sys.maxsize, sys.maxsize
        
        dfs(root)
        
        return self.res
        """
        if not root:
            return 0
        self.m = 1
        def dfs(node):
            if not node:
                return 0, 0, True, 0
            if not node.left and not node.right:
                return node.val, node.val, True, 1
            leftmin, leftmax, isleft, leftsize = dfs(node.left)
            rightmin, rightmax, isright, rightsize = dfs(node.right)
            if not isleft:
                return 0, 0, False, 0
            if not isright:
                return 0, 0, False, 0
            if isleft and isright:
                if node.left and node.right  and leftmax < node.val < rightmin:
                    self.m = max(self.m, leftsize + rightsize + 1)
                    return leftmin, rightmax, True, leftsize + rightsize + 1
            
                elif not node.right and node.left  and leftmax < node.val:
                    self.m = max(self.m, leftsize + 1)
                    return leftmin, node.val, True, leftsize + 1
                
                elif node.right and not node.left  and node.val < rightmin:
                    self.m = max(self.m, rightsize + 1)
                    return node.val, rightmax, True, rightsize + 1
                elif not node.left and not node.right:
                    return node.val, node.val, True, 1
            return 0, 0, False, 0
        dfs(root)
        return self.m
        """
        
        
