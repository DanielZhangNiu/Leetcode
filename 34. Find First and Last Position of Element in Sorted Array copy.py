
"""
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
    
    Your algorithm's runtime complexity must be in the order of O(log n).
    
    If the target is not found in the array, return [-1, -1].
    
    Example 1:
    
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:
    
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

"""

def searchRange(nums: 'List[int]', target: 'int') -> 'List[int]':
    if not nums: return [-1,-1]
        
    left, right = self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
    
def binarySearchLeft(A, x):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if x > A[mid]: left = mid +1
        else: right = mid -1
    return left

def binarySearchRight(A, x):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if x >= A[mid]: left = mid +1
        else: right = mid -1
    return right
