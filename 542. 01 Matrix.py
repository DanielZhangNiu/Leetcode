"""
    Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
    
    The distance between two adjacent cells is 1.
    
    
    
    Example 1:
    
    Input:
    [[0,0,0],
    [0,1,0],
    [0,0,0]]
    
    Output:
    [[0,0,0],
    [0,1,0],
    [0,0,0]]
    Example 2:
    
    Input:
    [[0,0,0],
    [0,1,0],
    [1,1,1]]
    
    Output:
    [[0,0,0],
    [0,1,0],
    [1,2,1]]
    
    
    Note:
    
    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.

"""
import collections
import heapq
def updateMatrix(matrix: List[List[int]]):
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
    if not matrix: return []
                
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    Q = []
    visited = set()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                heapq.heappush(Q,(0,i,j))
                visited.add((i,j))
                
    while Q:
        val, x, y  = heapq.heappop(Q)
        
    
        for dir in directions:
            nx, ny = x + dir[0], y + dir[1]
    
        while nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and (nx,ny) not in visited:
                matrix[nx][ny] = val + 1
                                            
            heapq.heappush(Q,(matrix[nx][ny],nx,ny))
            visited.add((nx,ny))
                
    return matrix
