"""
    You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
    
    
    
    Example 1:
    
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    Example 2:
    
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
    Example 3:
    
    Input: amount = 10, coins = [10]
    Output: 1
"""
def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
        
        TLE
        
    if not coins and amount == 0: return 1
    if not coins: return 0
        
    self.res = 0
        
        
    def backtrace(path, index, coins, target):
        if target < 0: return
        if target == 0:
        self.res += 1
        
        for i in range(index, len(coins)):
            backtrace(path+[coins[i]],i, coins, target - coins[i])
        
        backtrace([],0,coins,amount)
        return self.res
    """
            

        # n = number of types of coins
        # m = desired amount
        # f[i][j] = the number of combinations to make up amount j with the first i types of coins
        
        
    if not coins and amount == 0: return 1
    if not coins: return 0
                            
    #coins.sort()
    row, col = len(coins)+1 , amount+1
    dp = [[0] * col for _ in range(row)]
                        
    for i in range(len(coins)+1):
        dp[i][0] = 1
                                    
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
        # consider j as amount, i as coins, if amount even less than the coin, we not considerate it
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                                                            
    return dp[-1][-1]
