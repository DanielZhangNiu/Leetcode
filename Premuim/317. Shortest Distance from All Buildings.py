"""
 You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

 Each 0 marks an empty land which you can pass by freely.
 Each 1 marks a building which you cannot pass through.
 Each 2 marks an obstacle which you cannot pass through.
 Example:

 Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

 1 - 0 - 2 - 0 - 1
 |   |   |   |   |
 0 - 0 - 0 - 0 - 0
 |   |   |   |   |
 0 - 0 - 1 - 0 - 0

 Output: 7

 Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
              the point (1,2) is an ideal empty land to build a house, as the total
              travel distance of 3+3+1=7 is minimal. So return 7.
 Note:
 There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

"""
"""
Do a BFS from each building to find for each empty land its shortest distance to that particular building. Then we iterate over all empty lands and find for each land its sum of shortest distances to all buildings, and record the minimum value of such sums. Finally, we return the minimum value we recorded.

Time complexity: O(k*l), space complexity: O(m*n*k), where m = len(grid), n = len(grid[0]), k is the number of buildings in the grid, and l is the number of empty lands in the grid.
"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        self.matrix = collections.defaultdict(list)
        building = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    building += 1
                    self.bfs(grid, i,j)
        
        #print(self.matrix)
        res = sys.maxsize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                idx = tuple((i,j))
                if self.matrix[idx] and len(self.matrix[idx]) == building:
                    res = min(res, sum(self.matrix[idx]))
        return res if res!= sys.maxsize else -1
    
    def bfs(self,grid, r, c):
        Q = collections.deque([(0,r,c)])
        curlen = 0
        visited = set()
        visited.add((r,c))
        while Q:
            curlen, curx, cury = Q.popleft()
            for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
                i, j = curx + dir[0], cury + dir[1]
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]==0 and (i,j) not in visited:
                    Q.append((curlen+1, i , j))
                    idx = tuple((i,j))
                    if not self.matrix[idx]:
                        self.matrix[idx] = [curlen+1]
                    else:
                        self.matrix[idx].append(curlen+1)
                    visited.add((i,j))
