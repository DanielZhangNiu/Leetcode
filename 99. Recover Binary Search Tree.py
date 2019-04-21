
"""
    Two elements of a binary search tree (BST) are swapped by mistake.
    
    Recover the tree without changing its structure.
    
    Example 1:
    
    Input: [1,3,null,null,2]
    
    1
   /
  3
   \
    2
    
    Output: [3,1,null,null,2]
    
    3
   /
  1
   \
    2
    Example 2:
    
    Input: [3,1,4,null,null,2]
    
    3
   / \
  1   4
     /
    2
    
    Output: [2,1,4,null,null,3]
    
    2
   / \
  1   4
     /
    3
    
    Follow up:
    
    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def recoverTree(root):
    """
    Do not return anything, modify root in-place instead.
    
    Use whatever inorder traversal you like (recursion/stack = O(log n) extra space, Morris = O(1) extra space). As most people have figured out pretty easily, the idea is to remember the last value you saw and compare it with the current value. If lastValue > currentValue, then we know that something is "wrong", but it's not immediately clear which values have to be swapped.
    
    There are 2 cases: The values that need to be swapped are either adjacent or not adjacent. If they're adjacent, then there will be one "drop"; if they're not adjacent, then there will be two "drops".
    
    adjacent: ... _ < _ < A > B < _ < _ ...
                          ^^^^^
                          drop #1
    
    not adjacent: ... _ < _ < A > X < _ < Y > B < _ < _ ... (X may be the same as Y, but it's irrelevant)
                              ^^^^^       ^^^^^
                              drop #1     drop #2
    In both cases, we want to swap A and B. So the idea is to keep a drops array and append a tuple of (lastNode, currentNode) whenever we come across lastValue > currentValue. At the end of the traversal, the drops array must have either 1 or 2 tuples (otherwise, there would be more than 2 nodes that need to be swapped).
    

    """
    p, prev = root, TreeNode(float('-inf'))
    stack, drop = [], []
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            cur = stack.pop()
            if cur.val < prev:
                drop.append((prev,cur))
            prev, p = cur, cur.right

    drop[0][0].val, drop[-1][1].val = drop[-1][1].val, drop[0][0].val



