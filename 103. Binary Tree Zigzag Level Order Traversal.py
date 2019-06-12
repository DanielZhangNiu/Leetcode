
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

def zigzagLevelOrder(root):
    """
        :type root: TreeNode
        :rtype: List[List[int]]
       
    self.res = [];
    def dfs(root, depth):
    if not root:
            return
    if depth == len(self.res):
        self.res.append([])
    self.res[depth].append(root.val)
    dfs(root.left,depth+1)
    dfs(root.right,depth+1)

    dfs(root, 0)
    for i in range(1,len(self.res),2):
        self.res[i].reverse()
    return self.res
    
    """
    if not root: return []
    flag = False
    Q = collections.deque()
    Q.append(root)
    res = []
    while Q:
        nextQ, level = [],[]
        for node in Q:
            level.append(node.val)
            if node.left:
                nextQ.append(node.left)
            if node.right:
                nextQ.append(node.right)
        if flag: level.reverse()
        flag = not flag
        res.append(level)
        Q = nextQ
    return res
