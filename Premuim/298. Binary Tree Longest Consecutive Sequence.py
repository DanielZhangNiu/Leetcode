"""
 Given a binary tree, find the length of the longest consecutive sequence path.

 The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

 Example 1:

 Input:

    1
     \
      3
     / \
    2   4
         \
          5

 Output: 3

 Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
 Example 2:

 Input:

    2
     \
      3
     /
    2
   /
  1

 Output: 2

 Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        ret = 0
        stack = [(root, 1)]
        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append((node.left, cnt+1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cnt+1 if node.right.val == node.val + 1 else 1))
            ret = max(ret, cnt)
        
        return ret
