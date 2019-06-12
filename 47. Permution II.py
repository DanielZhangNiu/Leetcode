"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
 [1,1,2],
 [1,2,1],
 [2,1,1]
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
    visited = [0] * len(nums)
    def buildpath(nums,index,path,visited):
        if not nums:
            return
        if len(path) > len(nums):
            return
        if len(path) == len(nums) :
            res.append(path)

        for i in range(index, len(nums)):
            if i > 0 and visited[i-1] == 0 and nums[i]==nums[i-1]:
                continue
            if visited[i] = 0:
                visted[i] = 1
                buildpath(nums,index,path+[nums[i]],visited)
                visited[i] = 0

        buildpath(nums,0,[],visited)
        return res
