
"""
    Given a collection of distinct integers, return all possible permutations.
    
    Example:
    
    Input: [1,2,3]
    Output:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]
"""
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
        
    O(n * n!)
    """
            
    if not nums:
        return []
                
    res = []
    visited = set()
    def buildpath(nums,index,path,visited):
        if not nums:
            return
        if len(path) > len(nums):
            return
        if len(path) == len(nums) :
            res.append(path)

        for i in range(index, len(nums)):
            if i in visited:
                continue
            visited.add(i)
            buildpath(nums,index,path+[nums[i]],visited)
            visited.remove(i)
            buildpath(nums,0,[],visited)
        return res
