"""
    Given a non-empty binary tree, find the maximum path sum.
    
    For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
    
    Example 1:
    
    Input: [1,2,3]
    
    1
    / \
    2   3
    
    Output: 6
    Example 2:
    
    Input: [-10,9,20,null,null,15,7]
    
    -10
    / \
    9  20
    /  \
    15   7
    
    Output: 42

    
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    bottom up divide conquer，在返回的时候传入左右任意一边最大值加上目前root.val:
    cur = max(left, right) + root.val
    这种情况处理了从Root到左右任意一边的最大值，也就是 root.val + left 和 root.val + right
    还有一种情况就是当最大值 = root.val + left + right， 我们在放入global变量的时候何其比较。
    对于最底部叶子节点传上来的值，我们将其设置成0: return cur if cur > 0 else 0
    """
    if not root: return 0
    res = -sys.maxsize
    dfs(root)
    return res

def dfs(node):
    if not node: return 0
    left = right = 0
    if node.left:
        left = dfs(node.left)
    if node.right:
        right = dfs(node.right)
    tmax = node.val + max(left, right,0)
    ttma = node.val + left + right
    res = max(res, ttmax ,tmax)
    return tmax

