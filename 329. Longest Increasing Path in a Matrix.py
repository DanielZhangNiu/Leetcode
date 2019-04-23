"""
    Given an integer matrix, find the length of the longest increasing path.
    
    From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
    
    Example 1:
    
    Input: nums =
    [
    [9,9,4],
    [6,6,8],
    [2,1,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
    Example 2:
    
    Input: nums =
    [
    [3,4,5],
    [3,2,6],
    [2,2,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
def longestIncreasingPath(matrix: 'List[List[int]]') -> 'int':
    """
    We can find longest decreasing path instead, the result will be the same.
    Use dp to record previous results and choose the max dp value of smaller neighbors.
    """
        
        
    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    res =0
    for i in range(M):
        for j in range(N):
            res = max(res, self.dfs(i,j,matrix))
    return res
    
def dfs(i, j,matrix,dp):
    if dp[i][j] == 0:
        val = matrix[i][j]
        dp[i][j] = 1 + max(dfs(i - 1, j,matrix,dp) if i > 0 and val > matrix[i - 1][j] else 0,
                           dfs(i + 1, j,matrix,dp) if i < len(matrix) - 1 and val > matrix[i + 1][j] else 0,
                           dfs(i, j - 1,matrix,dp) if j > 0 and val > matrix[i][j - 1] else 0,
                           dfs(i, j + 1,matrix,dp) if j < len(matrix[0]) - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]
