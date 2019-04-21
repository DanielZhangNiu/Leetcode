
"""
    Given a set of distinct integers, nums, return all possible subsets (the power set).
    
    Note: The solution set must not contain duplicate subsets.
    
    Example:
    
    Input: nums = [1,2,3]
    Output:
    [
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
    ]

"""

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    
    子集个数一共 2^n，每个集合的平均长度是 O(n) 的
    O(n * 2^n)
    """
    self.res = []
            
    def dfs(nums,path,idx):
        if len(path) > len(nums): return
        self.res.append(path)
        for i in range(idx,len(nums)):
                
            dfs(nums,path+[nums[i]],i+1)
                    
                    
    dfs(nums,[],0)
    return self.res
