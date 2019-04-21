
"""
    You are climbing a stair case. It takes n steps to reach to the top.
    
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Note: Given n will be a positive integer.
    
    Example 1:
    
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:
    
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

"""

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    rolling array save space
    if n < 3:
        return n
    dp = [0] * 3
    dp[0], dp[1] = 1,2
    
    for i in range(2,n):
        dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
    return dp[(n-1)%3]
    """
    if n <= 3:
        return n
    dp = [0 for i in range(n)]
    dp[0],dp[1] = 1 , 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

