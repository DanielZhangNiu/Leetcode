"""
    Find the sum of all left leaves in a given binary tree.
    
    Example:
    
    3
    / \
    9  20
    /  \
    15   7
    
    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sumOfLeftLeaves(root):
    if not root:
        return 0
    def dfs(node):
        if not node: return
        if node.left and not node.left.left and node.left.right:
            self.res += node.left.val
        dfs(node.left)
        dfs(node.right)
    self.res = 0
    dfs(root)
    return self.res


