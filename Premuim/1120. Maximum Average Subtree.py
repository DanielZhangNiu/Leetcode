"""
 Given the root of a binary tree, find the maximum average value of any subtree of that tree.

 (A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

  

 Example 1:



 Input: [5,6,1]
 Output: 6.00000
 Explanation:
 For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
 For the node with value = 6 we have an average of 6 / 1 = 6.
 For the node with value = 1 we have an average of 1 / 1 = 1.
 So the answer is 6 which is the maximum.
  

 Note:

 The number of nodes in the tree is between 1 and 5000.
 Each node will have a value between 0 and 100000.
 Answers will be accepted as correct if they are within 10^-5 of the correct answer.
 Accepted
 6,942
 Submissions
 11,224
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def DFS(node):
            total, num = node.val, 1
            if node.left:
                acc, cnt = DFS(node.left)
                total += acc
                num += cnt
            if node.right:
                acc, cnt = DFS(node.right)
                total += acc
                num += cnt
                
            self.max_avg = max(self.max_avg, total / num)
            return total, num
        
        self.max_avg = float('-inf')
        DFS(root)
        return self.max_avg

