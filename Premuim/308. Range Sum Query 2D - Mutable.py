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
 update(3, 2, 2)
 sumRegion(2, 1, 4, 3) -> 10
 Note:

 The matrix is only modifiable by the update function.
 You may assume the number of calls to update and sumRegion function is distributed evenly.
 You may assume that row1 ≤ row2 and col1 ≤ col2.

"""
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]

        self.matrix = matrix
        """
        
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
       
        self.matrix[row][col] = val
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in range(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
