"""
    Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
    
    Example 1:
    
    Input:nums = [1,1,1], k = 2
    Output: 2
    Note:
    
    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""
def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
    还记得twosum这道题么？其实我们大可以把preSum作为我们字典中的key，然后value设置成为preSum出现次数，我们在迭代的时候，只需要查找preSum - target在不在字典里面，在的话，返回值增值即可，思路和two sum完全一样。这里我们字典里之所以存储出现次数，是为了解决出现重复数字的问题，比如
        [0,0,0]这种case。
            
        """
        count = preSum = 0
        hashMap = collections.defaultdict(lambda:0)
        for i in nums:
            hashMap[preSum] += 1    # put pre_sum into hashmap
            
            preSum += i
            if preSum-k in hashMap:
                count += hashMap[preSum-k]
    
    return count
