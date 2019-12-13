"""
  Input: 7
   Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
   Explanation:

    """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        :param N: A full binary tree must have odd number of nodes
        The number of leaf nodes must be N // 2 + 1
    
        """
        if N%2 == 0:
            return []
        if N == 1: return [TreeNode(0)]

        ret = []
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l): #traverse left subtree
                for right in self.allPossibleFBT(N - l -1): # traverse right subtree
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret.append(root)
            
        return ret
        
        
        
