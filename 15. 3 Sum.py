"""
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    
    Note:
    
    The solution set must not contain duplicate triplets.
    
    Example:
    
    Given array nums = [-1, 0, 1, 2, -1, -4],
    
    A solution set is:
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
    
"""
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
            
    nums.sort()
    res = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
                continue
        l = i + 1
        r = len(nums)-1
            
        while l < r:
            if nums[l] + nums[r] + nums[i] == 0:
                res.append((nums[i],nums[l],nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l +=1
                while l < r and nums[r] == nums[r-1]:
                    r -=1
                    
                r-=1
                l+=1
                elif nums[l] + nums[r]+ nums[i] > 0:
                    r -=1
                else:
                    l +=1
    return res
