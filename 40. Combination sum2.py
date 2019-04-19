
"""
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
    
    Each number in candidates may only be used once in the combination.
    
    Note:
    
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    Example 1:
    
    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
    ]
    Example 2:
    
    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
    [1,2,2],
    [5]
    ]
"""

def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return []
        
    candidates.sort()
    res=[]
    self.dfs(candidates,0,target,res,[])
    return res

def dfs(nums, index, goal, res, path):
    if goal<0:
        return
    if goal == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        if i > index and nums[i]==nums[i-1]:
            continue;
        self.dfs(nums,i+1, goal-nums[i],res,path+[nums[i]])
