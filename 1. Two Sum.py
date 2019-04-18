def twoSum(self, nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

    tmp = sorted(nums)
    left, right = 0, len(nums)-1
    while left < right:
        if tmp[left]+tmp[right] == target:
            return [nums.index(tmp[left]),nums.index(tmp[right])]

        elif tmp[left] + tmp[right] < target:
            left+=1
        else:
            right-=1
    return None
     """
    if not nums: return []
    hashmap = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp in hashmap:
            return [hashmap[tmp], i]
        else:
            hashmap[nums[i]] = i
    return [-1, -1]

print([2,7,11,13])