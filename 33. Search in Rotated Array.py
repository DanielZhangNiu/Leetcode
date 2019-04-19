
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


def search(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        
        tmp=nums[:]
        tmp.sort()
        l,r=0,len(tmp)-1
        while l<=r:
        mid=l+(r-l+1)//2
        if tmp[mid]==target:
        return nums.index(tmp[mid])
        elif tmp[mid]<target:
        l=mid+1
        else:
        r=mid-1
        return -1
    """
    start = 0
    end = len(nums)-1
    while(start <= end):
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
                            
        #decide target in which part
        if nums[start] <= nums[mid]:
        #left is in ascending order
            if nums[start] <= target and target < nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
        #right is in ascending order
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid -1
    return -1
