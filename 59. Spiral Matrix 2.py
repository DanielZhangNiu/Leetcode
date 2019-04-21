
"""
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    
    Example:
    
    Input: 3
    Output:
    [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
    ]

"""

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    array = [i for i in range(1,n*n+1)]
    nums = collections.deque(array)
    res = [[[0] for i in range(1,n+1)] for j in range(1,n+1)]
    left , right, up, down = 0, n, 0, n
        
    while left< right and up < down:
        # top
        for i in range(left,right):
            res[up][i] = nums.popleft()
            
        #right
        for i in range(up+1,down):
            res[i][right-1] = nums.popleft()
    
        #down
        for i in range(right-2,left, -1):
            res[down-1][i] = nums.popleft()
            
        #left
        for i in range(down-1,up,-1):
            res[i][left] = nums.popleft()
            
        up += 1
        left +=1
        right -=1
        down -=1
    return res

