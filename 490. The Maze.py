"""
    There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
    
    Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
    
    The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
    
    
    
    Example 1:
    
    Input 1: a maze represented by a 2D array
    
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0
    
    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (4, 4)
    
    Output: true
    
    Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    
    Example 2:
    
    Input 1: a maze represented by a 2D array
    
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0
    
    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (3, 2)
    
    Output: false
    
    Explanation: There is no way for the ball to stop at the destination.
    
    
    
    Note:
    
    There is only one ball and one destination in the maze.
    Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
    The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
    The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.


"""
import collections
def hasPath(maze, start, destination):

    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    
    
    DFS:
    if not maze or start == destination: return True
    
    self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    self.visited = set()
    self.visited.add((start[0],start[1]))
    def dfs(row, col, maze,destination):
        if row == destination[0] and col == destination[1]:
            return True
        self.visited.add((row,col))
        for dir in self.directions:
            nx, ny = row + dir[0], col + dir[1]
            while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                nx += dir[0]
                ny += dir[1]
    
                newr, newc = nx - dir[0], ny - dir[1]
                if (newr, newc) not in self.visited:
                    if dfs(newr, newc, maze, destination):
                        return True
    
                return False
    
    return dfs(start[0],start[1],maze,destination)
    
    """
        
        # BFS
        
    if not maze or start == destination: return True
        
    m, n = len(maze) ,len(maze[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    Q = collections.deque([start])
        
    visited = set()
    visited.add((start[0],start[1]))
        
    while Q:
        x,y = Q.popleft()
        # Roll the ball until it hits a wall or reach destination
        if x == destination[0] and y == destination[1]:
            return True
            
        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
            while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                nx += dir[0]
                ny += dir[1]
                
            # x and y locates at a wall when exiting the above while loop, so we need to backtrack 1 position
            # to reach the destination
            row, col = nx - dir[0], ny - dir[1]
                
            if (row,col) not in visited:
                Q.append([row,col])
                visited.add((row,col))

    return False
