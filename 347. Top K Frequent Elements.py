"""
    Given a non-empty array of integers, return the k most frequent elements.
    
    Example 1:
    
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    Example 2:
    
    Input: nums = [1], k = 1
    Output: [1]
    Note:
    
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
import collections
import heapq
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    dict = collections.Counter(nums)
    h = []
            
    for key,val in dict.items():
        heapq.heappush(h,(-val,key))
        
    res = [heapq.heappop(h)[1] for i in range(k)]
    return res


"""
Use dict to count the frequency of the numbers, then put them into a bucket where index represents frequency. The higher the index, the higher the frequency, so loop from the end of the bucket to build the return list. Scan through the list three times, so O(3n)
    
    dict = collections.Counter(nums)
  
        
    bucket = [[] for _ in range(len(nums)+1)]
    for key, val in dict.items():
        bucket[val].append(key)
        
    ret = []
    for row in reversed(bucket):
        if not row:
            continue
        else:
            for i in range(len(row)):
                ret.append(row[i])
                if len(ret) == k:
                    return ret
