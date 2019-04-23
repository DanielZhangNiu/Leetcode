"""
    You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    
    Example 1:
    
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    Example 2:
    
    Input: coins = [2], amount = 3
    Output: -1
    Note:
    You may assume that you have an infinite number of each kind of coin.
"""
def coinChange(coins: List[int], amount: int) -> int:
    
            
        dp = [0] + [float('inf')] * amount
            
        # dp = [0,0,0,0,0,0,0,0,0,0,0]
        for coin in coins:
            # 1
            for i in range(1, amount+1):
            # 1 ~ 12
                if i < coin: dp[i] = dp[i]  # if
                    else: dp[i] = min(dp[i], dp[i-coin]+1)  #dp[i-coin] means the sub problem we solved before, every dp[i] is a subproblems
#round 1, coin = 1, dp[1] = min(dp[1],dp[0]+1)= 1, dp[2] = min(dp[2],dp[1]+1) = 2 .... dp[11] = 11
# round 2, coin = 2, dp[2] = min(dp[2],dp[0]+1) = 2, dp[3] = min(dp[3], dp[1]+1) =2
            

return dp[-1] if dp[-1] != float('inf') else -1
            

