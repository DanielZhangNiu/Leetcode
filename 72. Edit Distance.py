
"""
    Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
    
    You have the following 3 operations permitted on a word:
    
    Insert a character
    Delete a character
    Replace a character
    Example 1:
    
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
    Example 2:
    
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')


"""
def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
        -----------------
        |replace| insert|
        |----------------
        | delete| result|
        |-----------------
        
    if the current char of word1 != current char of word2:
        Take the minimum from replace, insert and delete then + 1
        
    elif char1 == char2:
        Just take the number of replace from previous result, since we don't need to do operation
    
    example:
        
        ""  h   o   r   s   e
        
    ""  0   1   2   3   4   5
        
    r   1  0+1 1+1  2  2+1 3+1
        
    o   2  1+1  1  1+1 2+1 3+1
    
    s   3  2+1 1+1 1+1  2  2+1    : the result is 2+1 = 3
        
    """
    l1, l2 = len(word1)+1, len(word2)+1
    dp = [[0 for _ in range(l2)] for _ in range(l1)]
    for i in range(l1):
        dp[i][0] = i
    for j in range(l2):
        dp[0][j] = j
    for i in range(1, l1):
        for j in range(1, l2):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[-1][-1]
                                                        
                                                        
        """
        Naive recursive solution  TLE
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return (word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)
        """
