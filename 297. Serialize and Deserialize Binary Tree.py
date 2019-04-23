
"""
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
    
    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
    
    Example:
    
    You may serialize the following tree:
    
     1
    / \
   2   3
      / \
     4   5
    
    as "[1,2,3,null,null,4,5]"
    Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
    
    Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
    

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
            
            :type root: TreeNode
            :rtype: str
            """
        self.res = []
        def preorder(root):
            if root is None:
                self.res.append('x')
                return
            
            self.res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ','.join(self.res)
    
    # 1,2,x,x,3,4,x,x,5,x,x
    def deserialize(self, data):
        """Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
            """
        
        nodes = data.split(',')
        data = collections.deque(nodes)
        
        def dfs(data):
            if not data: return None
            while data[0] == 'x':
                data.popleft()
                return None
            root = TreeNode(data.popleft())
            root.left = dfs(data)
            root.right = dfs(data)
            
            return root
        
        return dfs(data)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
