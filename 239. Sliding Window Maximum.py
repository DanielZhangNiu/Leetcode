
"""
    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
    
    Example:
    
    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
    
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7      3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7
    Note:
    You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
    
    Follow up:
    Could you solve it in linear time?

"""
import collections
def maxSlidingWindow(nums, k):
    
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
        
        
    if len(nums) < k or not nums:
        return []
    res = [0] * (len(nums)-k + 1)
    for i in range(0,len(res)):
        res[i] = max(nums[i:i+k])
    return res
    """
    # base cases
    if not nums: return []
    if k <= 1: return nums
    
    # Defining Deque and result list
    queue = collections.deque()
    res = []

    # First traversing through K in the nums and only adding maximum value's index to the deque.
    # Note: We are only storing the index, not the value.
    # Comparing the new value in the nums with the last index value from deque,
    # and if new valus is less, we don't need it
    for i in range(k):
        while queue:
            if not nums[i] > nums[queue[-1]]:
                queue.pop()
            else:
                break
        queue.append(i)


    # Here we will have deque with index of maximum element for the first subsequence of length k.
    # Now we will traverse from k to the end of array and do 4 things
    # Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
    for i in range(k, len(nums)):
        # 1. Appending left most indexed value to the result
        res.append(nums[queue[0]])
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        if queue[0] < i - k + 1:
            queue.popleft()

        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it

        while queue:
            if not nums[i] > nums[queue[-1]]:
                queue.pop()
            else:
                break
        queue.append(i)
 
   #Adding the maximum for last subsequence
    res.append(nums[queue[0])
    return res


