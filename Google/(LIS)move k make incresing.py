   """
   Given an array, please check if we can remove at most k element to make it strictly increasing.

   Example 1:

   Input: [1, 2, 3, 7, 5, 6], k = 1
   Output: true
   Example 2:

   Input: [1, 2, 3, 7, 8, 4, 5] , k = 1
   Output: false
   
   
   return len(arr) - len(LIS) >= K
   Binary search思路
   在1,3,5,2,8,4,6这个例子中，当到6时，我们一共可以有四种
   (1)不同长度
   (2)且保证该升序序列在同长度升序序列中末尾最小
   的升序序列

   1
   1,2
   1,3,4
   1,3,5,6
   这些序列都是未来有可能成为最长序列的候选人。这样，每来一个新的数，我们便按照以下规则更新这些序列

如果nums[i]比所有序列的末尾都大，或等于最大末尾，说明有一个新的不同长度序列产生，我们把最长的序列复制一个，并加上这个nums[i]。
   如果nums[i]比所有序列的末尾都小，说明长度为1的序列可以更新了，更新为这个更小的末尾。
   如果在中间，则更新那个末尾数字刚刚大于等于自己的那个序列，说明那个长度的序列可以更新了。
   比如这时，如果再来一个9，那就是第三种情况，更新序列为

   1
   1,2
   1,3,4
   1,3,5,6
   1,3,5,6,9
   如果再来一个3，那就是第二种情况，更新序列为

   1
   1,2
   1,3,3
   1,3,5,6
   如果再来一个0，那就是第一种情况，更新序列为

   0
   1,2
   1,3,3
   1,3,5,6
   前两种都很好处理，O(1)就能解决，主要是第二种情况，实际上我们观察直到6之前这四个不同长度的升序序列，他们末尾是递增的，所以可以用二分搜索来找到适合的更新位置。
   
   """
class Solution:
    def LIS(nums, K):
        if not nums: return 0
        
        def findleft(nums, l, r , target):
            while l <= r:
                mid = (l + r ) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
            
        length = 0
        tails = [0] * len(nums)
        tails[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < tails[0]:
                tails[0] = nums[i]
            elif nums[i] > tails[length]:
                length += 1
                tails[length] = nums[i]
            else:
                idx = findleft(nums, 0, length, nums[i])
                tails[idx] = nums[i]
                
        return len(nums) - length - 1 >= K
        
        
