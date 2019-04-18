"""
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
    
    Example:
    
    Given array nums = [-1, 2, 1, -4], and target = 1.
    
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
"""
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    tmp=nums[0]+nums[1]+nums[2]
    for i in range(0,len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
            
    l,r = i+1, len(nums)-1
    while l < r:
        res=nums[i]+nums[l]+nums[r]
        if res == target:
            return res
            
        if abs(res-target)< abs(tmp-target):
            tmp=res
                
        if res < target:
            l+=1
        elif res>target:
            r-=1
    return tmp
