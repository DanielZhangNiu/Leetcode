"""
 You are given a m x n 2D grid initialized with these three possible values.

 -1 - A wall or an obstacle.
 0 - A gate.
 INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
 Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 Example:

 Given the 2D grid:

 INF  -1  0  INF
 INF INF INF  -1
 INF  -1 INF  -1
   0  -1 INF INF
 After running your function, the 2D grid should be:

   3  -1   0   1
   2   2   1  -1
   1  -1   2  -1
   0  -1   3   4
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) < 1:
            return
        queue = collections.deque()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j))
    # queue = [(i,j)]
        while queue:
        
            r, c = queue.popleft()
            for dir in direction:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < len(rooms) and 0 <= nc <len(rooms[0]) and rooms[nr][nc] > 2**30:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr,nc))
    