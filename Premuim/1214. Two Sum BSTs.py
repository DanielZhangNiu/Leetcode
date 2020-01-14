"""
 Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

  

 Example 1:



 Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
 Output: true
 Explanation: 2 and 3 sum up to 5.
 Example 2:



 Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
 Output: false
  

 Constraints:

 Each tree has at most 5000 nodes.
 -10^9 <= target, node.val <= 10^9

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """
        def dfs(n1, n2):
            if not n1 or not n2:
                return False
            if n1.val + n2.val < target:
                return dfs(n1.right, n2) or dfs(n1, n2.right)
            elif n1.val + n2.val > target:
                return dfs(n1.left, n2) or dfs(n1, n2.left)
            else:
                return True
        return dfs(root1, root2)
        """
        
        stack1, stack2 = [] , []
        while True:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.right
            if not stack1 or not stack2: return False
            
            if stack1[-1].val + stack2[-1].val == target:
                return True
            elif stack1[-1].val + stack2[-1].val > target:
                node = stack2.pop()
                root2 = node.left
            else:
                node = stack1.pop()
                root1 = node.right
            
            
        
