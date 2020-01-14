"""
 You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

 You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

 Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

 Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

  

 Example 1:

 Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
 Output: 6
 Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
 Example 2:

 Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
 Output: 1
 Explanation: There is only one way to cut the bar into 9 pieces.
 Example 3:

 Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
 Output: 5
 Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
  

 Constraints:

 0 <= K < sweetness.length <= 10^4
 1 <= sweetness[i] <= 10^5
"""
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # same as No.410 use binary search to minimize the sum of subsets we could divide
        # we want maximum total sweetness K+1 pieces, which means to maximize the smallest sum among these k+1 subarrays, this is the different with No.410
        if len(sweetness) == K + 1: return min(sweetness)
        if len(sweetness) < K + 1:  return -1
        
        left, right = min(sweetness) , sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if self.isvalid(sweetness, mid, K+1):
                right = mid - 1
            else:
                left = mid + 1
        
        return left if self.isvalid(sweetness, left, K+1 ) else right


    """
    二分找最大值，isvalid找最小的subset

    找最小的subset，需要尽量增大subset，看有多少这样的subset满足条件，如果按照这样分subset的数量小于等于K，说明这样分是valid的
    """
    def isvalid(self, nums, mid, K):
        
        cursum, cntofset = 0, 1
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum > mid:
                cursum = 0
                cntofset+=1
                if cntofset > K: return False
        
        return cntofset <= K
        
