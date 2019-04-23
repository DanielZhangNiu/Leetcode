"""
    There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
    
    Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
    
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
    
    Output: 12
    
    Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
    The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
    
    Example 2:
    
    Input 1: a maze represented by a 2D array
    
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0
    
    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (3, 2)
    
    Output: -1
    
    Explanation: There is no way for the ball to stop at the destination.
    
    
    
    Note:
    
    There is only one ball and one destination in the maze.
    Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
    The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
    The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""
import collections
import heapq
def shortestDistance(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    Why using PriorityQueue?
        
    We can consider this question as a shortest-route graph problem, that is, each stoppable point is a vertex, where every possible path between two nodes is an edge.
    In this way, we can using Dijkstra algorithm to solve this problem, and that's why we use PriorityQueue.
    """
    # Dijkstra Algorithm
    if not maze or start == destination: return 0
                
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    Q = []
    heapq.heappush(Q,(0, start))
    visited = {(start[0],start[1]):0}
                
    while Q:
        cur_len, cur = heapq.heappop(Q)
        x , y = cur[0],cur[1]
                
        if x == destination[0] and y == destination[1]:
            return cur_len
                            
        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
            dist = 0
            while nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0:
                nx += dir[0]
                ny += dir[1]
                dist += 1
            row, col = nx - dir[0], ny - dir[1]
                                            
            if (row,col) not in visited or dist + cur_len < visited[(row,col)]:
                heapq.heappush(Q,(cur_len + dist, (row,col)))
                visited[(row,col)] = cur_len + dist
                                                    
    return -1
