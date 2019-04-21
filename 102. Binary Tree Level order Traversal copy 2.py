
"""
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
    
    For example:
    Given binary tree [3,9,20,null,null,15,7],
    
    3
   / \
  9  20
    /  \
   15   7
    return its level order traversal as:
    
    [
    [3],
    [9,20],
    [15,7]
    ]


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    def buildpath(root, depth):
        if not root:
            return
        if len(self.res) == depth:
            self.res.append([])
        
        self.res[depth].append(root.val)
        buildpath(root.left , depth+1)
        buildpath(root.right , depth+1)
        
    self.res = []
    buildpath(root,0)
    return self.res
        
        
        
        """
        if not root:return []
        queue = [root]
        res = []
        while queue:
            path = []
            for i in range(len(queue)):  # every level
                node = queue.pop(0)
                path.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(path)

        return res

