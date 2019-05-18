"""
    You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
    
    Example 1:
    
    Input: [4, 1, 8, 7]
    Output: True
    Explanation: (8-4) * (7-1) = 24
    Example 2:
    
    Input: [1, 2, 1, 2]
    Output: False
    Note:
    
    The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

"""
 def judgePoint24(nums: List[int]) -> bool:
    """
 
    DFS, make any two of the element into new element, push into previous condidates,
    make decision when there is only one element left, compare this double value with 24
    
    """
    if not nums: return False
    return self.dfs(nums)

def dfs(self, nums):
    if len(nums) == 1 and abs(nums[0] - 24) <= 0.001:
        return True

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i == j: continue
            a, b = nums[i],nums[j]
            possible = [a+b, a-b, b-a,a*b]
            if a: possible.append(b/a)
            if b: possible.append(a/b)
            base = [nums[k] for k in range(len(nums)) if k!= i and k!=j]

            for op in possible:
                base.append(op)
                if self.dfs(base):
                    return True
                base.pop()
    return False


