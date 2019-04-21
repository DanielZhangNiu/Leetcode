
"""
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    
    Example 1:
    
    Input:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
    
    Example 2:
    
    Input:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix: return []
    left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
    res = []
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        for j in range(top, bottom):
            res.append(matrix[j][right])
        for k in range(right,left, -1):
            res.append(matrix[bottom][k])
        for l in range(bottom,top,-1):
            res.append(matrix[l][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1
    #single squre
        if left == right and top == down:
            res.append(matrix[up][left])
    # vertical line
        elif left == right:
            for i in range(top, down):
                res.append(matrix[i][left])
        elif top == bottom:
            for j in range(top, down):
                res.append(matrix[top][i])
        return res





    
            

