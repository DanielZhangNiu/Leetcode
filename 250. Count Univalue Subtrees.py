"""
    Given a binary tree, count the number of uni-value subtrees.
    
    A Uni-value subtree means all nodes of the subtree have the same value.
    
    Example :
    
    Input:  root = [5,1,5,5,5,null,5]
    
     5
    / \
   1   5
  / \   \
 5   5   5
    
    Output: 4

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def countUnivalSubtrees(root: TreeNode) -> int:
   
    self.res = 0
    isunique(root)
    return self.res

def isunique(node):
    if not node:
        return True
    l, r = isunique(node.left), isunique(node.right)
    if l and r and(not node.left or node.left.val == node.val) and(not node.right or node.right.val == node.val):
        self.res+=1
        return True
    return False

