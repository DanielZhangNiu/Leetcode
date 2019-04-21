
"""
    Given a binary tree, return the inorder traversal of its nodes' values.
    
    Example:
    
    Input: [1,null,2,3]
   1
    \
     2
    /
   3
    
    Output: [1,3,2]
    Follow up: Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def inorderTraversal(root):
    """
    Recursive
    if not root: return None
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    """
    if not root: return None
    stack = []
    res = []
    p = root
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            node = stack.pop()
            res.append(node.val)
            p = node.right
    return res

