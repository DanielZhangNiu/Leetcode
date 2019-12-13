"""
   Given a positive integer n, find out how many ways of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition.

    Example:

    Input: 5
    Output: 6
    Explanation:
    1. 1 + 1 + 1 + 1 + 1
    2. 1 + 1 + 1 + 2
    3. 1 + 1 + 3
    4. 1 + 4
    5. 1 + 2 + 2
    6. 2 + 3
    
    
    Coin change 2 , 0/1 knapsack problem
    """
class Solution:
    def change(amount: int) -> int:
        if amount == 0 and : return 0
        nums = [i+1 for i in range(amount)]
        dp = [[0 for j in range(amount + 1 )] for i in range(nums + 1 )]
        
        for i in range(len(nums+1)):
            dp[i][0] = 1
            
        for i in range(1, len(nums + 1 )):
            for j in range(1, len(amount + 1 )):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1] - 1 # exclude the amount itself
        
        
        
