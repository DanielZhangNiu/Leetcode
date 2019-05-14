"""
    Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
    
    
    
    Note:
    
    Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.
    
    
    
    Example:
    
    Given the following 3x6 height map:
    [
    [1,4,3,1,3,2],
    [3,2,1,3,2,4],
    [2,3,3,2,3,1]
    ]
    
    Return 4.
    
    
    The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
    
    
    
    
    
    After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
    


"""
import heapq
def trapRainWater(heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    if not heightMap or not heightMap[0]:
        return 0
        
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    m, n = len(heightMap), len(heightMap[0])
    heap = []
    visited = set()
    # Push all the blocks on the border into heap. And create a visit array.
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n -1 :
                heapq.heapqpush(heap,(heightMap[i][j],i,j))
                visited.add((i,j))
    res = 0
    while heap:
        cur_height, x, y = heapq.heappop(heap)
        for dir in direction:
            r, c = x + dir[0], y + dir[1]
            if r < 0 or r >=m or c < 0 or c >= n or (r,c) in visited:
                continue
            res += max(0,cur_height - heightMap[r][c])
            heapq.heapqpush(heap,(max(cur_height,heightMap[r][c]),r,c))
            visited.add((r,c))
    return res




