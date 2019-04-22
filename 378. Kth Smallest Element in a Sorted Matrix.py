"""
    Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
    
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.
    
    Example:
    
    matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],
    k = 8,
    
    return 13.
    Note:
    You may assume k is always valid, 1 ≤ k ≤ n2.


"""
def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
        
        
    output = []
    for row in matrix:
    output += row
    return sorted(output)[k - 1]
    
    Use Binary search idea to locate "left" the first required element,
    helper function countlessequal use to compare with K
    """
    if not matrix: return 0
    left, right = matrix[0][0], matrix[-1][-1]
    while left <= end:
        mid = left + (right - left)//2
        count = countlessequal(matrix, mid) # count how many element less or equals to mid
        if count < k:
            left = mid + 1
        else:
            right = mid - 1
    if countlessequal(matrix, left) >= k:
        return left

def countlessequal(matrix, val):   # similar with search in matrix, the left down element first
    i,j,count = len(matrix) - 1, 0, 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > val:
            i-=1
        else:
            count += i + 1
            j += 1
    return count

