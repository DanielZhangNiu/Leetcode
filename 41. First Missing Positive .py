
"""
    Given an unsorted integer array, find the smallest missing positive integer.
    
    Example 1:
    
    Input: [1,2,0]
    Output: 3
    Example 2:
    
    Input: [3,4,-1,1]
    Output: 2
    Example 3:
    
    Input: [7,8,9,11,12]
    Output: 1
    Note:
    
    Your algorithm should run in O(n) time and uses constant extra space.
"""
def firstMissingPositive(nums: List[int]) -> int:
    """
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
        the range [1,...,l+1]
        
        res = 1
        while res in nums:
            res += 1
        return res
        """
        
        N = len(nums)
        for i in range(N):
            while 1 <= nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1

# Time: O(N)
# Space: O(1)
