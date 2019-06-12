
"""
    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
    
    Example:
    
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Note: Please solve it without division and in O(n).
    
    Follow up:
    Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
            
            
        n = len(nums)
        res= [1 for _ in range(n)]
        f,b = 1,1
        for i in range(n):
            res[i]*=f
            res[n-1-i]*=b
            f*=nums[i]
            b*=nums[n-1-i]
        return res
        
first time going through the array, it's beginning to the end. p keeps a running total of the product, and each element will equal the running total of the products of the elements that came before. then the 2nd time going through the array, you're doing the same process, but backwards, finishing off the result by multiplying the elements that came after.
            """
        output=[1]  * len(nums)
        acc=1
        for i in range(len(nums)):
            output[i] = output[i] * acc
            acc = acc * nums[i]
        print(output)
        acc = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * acc
            acc = acc * nums[i]
        return output
