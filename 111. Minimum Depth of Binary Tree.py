
"""
    Given a binary tree, find its maximum depth.
    
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Given binary tree [3,9,20,null,null,15,7],
    
    3
   / \
  9  20
    /  \
   15   7
   
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    
        
    if not root:
        return 0
    if root.left==None or root.right==None:
        return self.minDepth(root.left)+self.minDepth(root.right)+1
    return min(self.minDepth(root.right),self.minDepth(root.left))+1
        """
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
