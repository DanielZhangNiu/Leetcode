"""
 Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
 The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
 Note: You can only put the bomb at an empty cell.

 Example:

 Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
 Output: 3
 Explanation: For the given grid,

 0 E 0 0
 E 0 W E
 0 E 0 0

 Placing a bomb at (1,1) kills 3 enemies.
"""
class Solution:

"""
Move right to left and back, same as top to down
We can perform an optimization: we can create a 2D array. For row wise direction, we can simply count the number of enemies between two walls, and then each value between 2 walls will be increased by the count of the enemies. A similar thing can be done column wise.
"""
    def process_left_right(self, i, grid):
        cnt, N, M = 0, len(grid), len(grid[0])
        for j in range(M):
            if grid[i][j] == "W":
                cnt = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                self.dp[i][j] += cnt
        
        return
    def process_right_left(self, i, grid):
        cnt, N, M = 0, len(grid), len(grid[0])
        for j in range(M-1, -1, -1):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                self.dp[i][j] += cnt
        
        return

    def process_up_down(self, j, grid):
        cnt, N, M = 0, len(grid), len(grid[0])
        for i in range(N):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                self.dp[i][j] += cnt
        return

    def process_down_up(self, j, grid):
        cnt, N, M = 0, len(grid), len(grid[0])
        for i in range(N-1, -1, -1):
            if grid[i][j] == "W":
                cnt  = 0
            elif grid[i][j] == "E":
                cnt += 1
            else:
                self.dp[i][j] += cnt
        return

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        N, M = len(grid), len(grid[0])
        self.dp = [[0 for i in range(M)] for _ in range(N)]
        self.max_bomb_enemy = 0
        for i in range(N):
            self.process_left_right(i, grid)
            self.process_right_left(i, grid)
        for j in range(M):
            self.process_up_down(j, grid)
            self.process_down_up(j, grid)

        for i in range(N):
            if self.dp[i]:
                self.max_bomb_enemy = max(self.max_bomb_enemy, max(self.dp[i]))
        
        return self.max_bomb_enemy
                

                
