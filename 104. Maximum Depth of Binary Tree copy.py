
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
   
return its depth = 3.
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
        二叉树节点个数为 N，每个节点上的计算时间为 O(1)。总的时间复杂度为 O(N)
        
    if root is None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        """
            
            
    depth = 0
    queue = [root] if root else []
    while queue:
        depth += 1
        for i in range(len(queue)):
            el = queue.pop(0)
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
                                            
    return depth
