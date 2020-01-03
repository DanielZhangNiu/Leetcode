"""
 Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

 Note:

 Given target value is a floating point.
 You are guaranteed to have only one unique value in the BST that is closest to the target.
 Example:

 Input: root = [4,2,5,1,3], target = 3.714286

     4
    / \
   2   5
  / \
 1   3

 Output: 4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root: return -1
        stack = []
        res = sys.maxsize
        tmp = sys.maxsize
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                cur = stack.pop()
                if abs(target - cur.val) < res:
                    tmp = cur.val
                    res = abs(target - cur.val)
                root = cur.right
        return tmp
