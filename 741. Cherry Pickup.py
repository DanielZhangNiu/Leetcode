"""
    In a N x N grid representing a field of cherries, each cell is one of three possible integers.
    
    
    
    0 means the cell is empty, so you can pass through;
    1 means the cell contains a cherry, that you can pick up and pass through;
    -1 means the cell contains a thorn that blocks your way.
    
    
    Your task is to collect maximum number of cherries possible by following the rules below:
    
    
    
    Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
    After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
    When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
    If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
    
    
    
    
    Example 1:
    
    Input: grid =
    [[0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]]
    Output: 5
    Explanation:
    The player started at (0, 0) and went down, down, right right to reach (2, 2).
    4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
    Then, the player went left, up, up, left to return home, picking up one more cherry.
    The total number of cherries picked up is 5, and this is the maximum possible.
    
    
    Note:
    
    grid is an N by N 2D array, with 1 <= N <= 50.
    Each grid[i][j] is an integer in the set {-1, 0, 1}.
    It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
    

"""
    def cherryPickup(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            
        (0,0) to (n-1,n-1) to (0,0) is the same as (n-1,n-1) to (0,0) twice
            
        1. two people start from(n-1,n-1) to (0,0) together (bottom up )
        2. they move one step simultanously(left or up), and pick up the cherry within the grid
        3. if they end up at same grid, only one of them will pick up the cherry
            
        dp/recursion with memoization
        x1, y1, x2 to represent a state ( y2 = x1 + y1 - x2) because only left or up  and move one step, so x1 + y1 == x2 + y2
            
        dp(x1,y1,x2) computes the max cherries if staret from {(x1,y1),(x2,y2)} to (0,0)
        dp(x1,y1,x2) = grid[y1][x1]+grid[y2][x2] + max(dp(x1-1,y1,x2-1),dp(x1,y1-1,x2-1),dp(x1-1,y1,x2),dp(x1,y1-1,x2))  note(x1,y1) cannot move at the same time, so four combinations there
            
        time and space: o(n^3)
        """
        
        self.grid = grid
        n = len(self.grid)
        mem = [[[None for i in range (n)] for j in range (n)] for k in range (n)]
        return max(0,self.dp_result(n-1,n-1,n-1,mem))
    
    def dp_result(self,x1, y1, x2, mem):
        y2 = x1 + y1 - x2
        if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0: return -1 #out of boundry, no solution
        if self.grid[y1][x1] == -1 or self.grid[y2][x2] == -1: return -1 #  -1 cell
        if x1 == 0 and y1 == 0: return self.grid[y1][x1]  #arrive the uppermost at the same time
        if mem[x1][y1][x2]!= None: return mem[x1][y1][x2] # already calculated
        
        res = max(self.dp_result(x1-1,y1,x2-1,mem),self.dp_result(x1,y1-1,x2-1,mem),self.dp_result(x1,y1-1,x2,mem),self.dp_result(x1-1,y1,x2,mem)) #max of four scenarios
        
        if res < 0:  # the current sub problme have no solution
            mem[x1][y1][x2] =-1
            return mem[x1][y1][x2]
        
        res += self.grid[y1][x1]  # pick up this cherry
        
        if x1!=x2:
            res+= self.grid[y2][x2] # two people not in same cell, so second people pick up the cherry
        
        mem[x1][y1][x2] = res
        return mem[x1][y1][x2]
