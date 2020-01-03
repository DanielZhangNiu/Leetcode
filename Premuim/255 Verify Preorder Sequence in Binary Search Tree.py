"""
    Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

    You may assume each number in the sequence is unique.

    Consider the following binary search tree:

         5
        / \
       2   6
      / \
     1   3
    Example 1:

    Input: [5,2,6,1,3]
    Output: false
    Example 2:

    Input: [5,2,1,3,6]
    Output: true
    Follow up:
    Could you do it using only constant space complexity?
"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        THOUGHT: We first look at the property of preorder traversal: we print left child’s value of current node all the way until we reached a leaf node (you will see numbers decreasing), then we start printing the value of a node (let it be rc) which is the right child of one of the nodes (let it be node p) we already traversed. When do you know it's a right child node's value? It's when you see a value greater than the last one. Also,till here we know, all the nodes in p’s left subtree have been read in the serialized array, and this property is maintained:

left subtree ‘s value < p ’s value < rc’s value
Since all the nodes whose value is smaller than p are already read, all the nodes’ value to be read after should have greater value than p’s value, so p’s value becomes the lower bound for any upcoming node.

p ’s value < upcoming value in array
Otherwise, it’s not valid. So the key here is to find the lower bound for upcoming nodes, which equals to find p.
        """
        stack = []
        lower = -sys.maxsize
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True
