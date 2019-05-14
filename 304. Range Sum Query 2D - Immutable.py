"""
    Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    
    Range Sum Query 2D
    The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
    
    Example:
    
    Given matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]
    
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
    Note:
    
    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
class NumMatrix:
    """
        # (0,0)
        # ---------------------------
        # |                         |
        # |           (r1,c1)       |
        # |             |-----------|(r1,c2)
        # |             |  RegionA  |
        # | ------------------------|(r2,c2)
        # |           (r2,c1)       |
        #  --------------------------
        #  RegionA = region(0,0 to r2,c2) -
        #       region(0,0 to r2,c1) -
        #       region(0,0 to r1,c2) +
        #       region(0,0 to r1,c1)
        """
def __init__(self, matrix):
    """
    :type matrix: List[List[int]]
            
    build a dynamic like sum matrix first, store the area in each cell.
    """
    n_row = len(matrix)
    n_col = len(matrix[0]) if n_row > 0 else 0
        
    self.sum_matrix = [[0 for i in range(n_col)] for j in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            top = self.sum_matrix[i][j - 1] if j > 0 else 0
            left = self.sum_matrix[i - 1][j] if i > 0 else 0
            topleft = self.sum_matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
            self.sum_matrix[i][j] = matrix[i][j] + top + left - topleft


def sumRegion(self, row1, col1, row2, col2):
    """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
            left = self.sum_matrix[row2][col1 - 1] if col1 > 0 else 0
            top = self.sum_matrix[row1 - 1][col2] if row1 > 0 else 0
            topleft = self.sum_matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
            return self.sum_matrix[row2][col2] + topleft - top - left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
