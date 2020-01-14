"""
 Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

  

 Example 1:

 Input: A = [4,7,9,10], K = 1
 Output: 5
 Explanation:
 The first missing number is 5.
 Example 2:

 Input: A = [4,7,9,10], K = 3
 Output: 8
 Explanation:
 The missing numbers are [5,6,8,...], hence the third missing number is 8.
 Example 3:

 Input: A = [1,2,4], K = 3
 Output: 6
 Explanation:
 The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
  

 Note:

 1 <= A.length <= 50000
 1 <= A[i] <= 1e7
 1 <= K <= 1e8
 Accepted
 7,862
 Submissions
 14,570
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if nums[-1] -nums[0]-1-len(nums)+2<k:
            k = k - (nums[-1]-nums[0]-len(nums)+1)
            return nums[-1]+k
        i, j  = 0, len(nums)-1
        while i+1 < j:
            m = i+ (j-i)//2
            if nums[m] - nums[i]-1-(m-i+1)+2<k:
                k = k- (nums[m] - nums[i]-m+i)
                i = m
            else:
                j = m
        return nums[i]+k
