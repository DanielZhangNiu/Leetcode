"""
 
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    
    Your algorithm should run in O(n) complexity.
    
    Example:
    
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
            
1: convert the list nums to a set. This takes O(n)
2: randomly pick one element e, check upwards if e+1, e+2, etc... is in the set. Similarly, check downwards if e-1, e-2,...etc is in the set
3. remove all the above ...e-1, e, e+1,... from the set, since we already "checked" these numbers and no need to check again.
4. repeat 2~3 until the set is empty
For step 2~4, each element can only be "checked" once so it's also O(n)

    """
        
    longest_consecutive = 0
        
    # put all numbers into a set
    distinct_numbers = set(nums)
        
    while distinct_numbers:
        # each number itself has a consecutive count of 1
        consecutive = 1
        
        # we will pop any number
        number = distinct_numbers.pop()
        
        # let's find all consecutive numbers higher than "number"
        next_number = number + 1
        while next_number in distinct_numbers:
            distinct_numbers.remove(next_number)
            next_number += 1
            consecutive += 1
        
        # let's find all consecutive numbers lower than "number"
        next_number = number - 1
        while next_number in distinct_numbers:
            distinct_numbers.remove(next_number)
            next_number -= 1
            consecutive += 1
        
        # update longest_consecutive accordingly
        longest_consecutive = max(longest_consecutive, consecutive)
        return longest_consecutive




"""
    :type nums: List[int]
    :rtype: int
    
    if len(nums) == 0:
    return 0
    if len(set(nums))==1:
    return 1
    nums.sort()
    maxlen,tmp = 0, 1
    for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 1:
    tmp+=1
    maxlen = max(maxlen,tmp)
    elif nums[i+1] == nums[i]:
    continue
    else:
    tmp = 1
    maxlen = max(maxlen,tmp)
    return maxlen
    
    
    nums = set(nums)
    maxlen = 0
    while nums:
    first = last = nums.pop()
    while first - 1 in nums:
    first -= 1
    nums.remove(first)
    while last + 1 in nums:
    last += 1
    nums.remove(last)
    maxlen = max(maxlen, last - first + 1)
    return maxlen
"""
