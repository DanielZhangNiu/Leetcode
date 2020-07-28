"""
 In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

 Then, a value from arr was removed that was not the first or last value in the array.

 Return the removed value.

  

 Example 1:

 Input: arr = [5,7,11,13]
 Output: 9
 Explanation: The previous array was [5,7,9,11,13].
 Example 2:

 Input: arr = [15,13,12]
 Output: 14
 Explanation: The previous array was [15,14,13,12].
  

 Constraints:

 3 <= arr.length <= 1000
 0 <= arr[i] <= 10^5


"""

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        flag = 0
        if arr[0] > arr[1]:
            flag = 1
        
        res = [0] * (len(arr))
        for i in range(1,len(arr)):
            res[i] = arr[i] - arr[i-1]
        res.pop(0)
        
        big, small = max(res), min(res)
        bigidx,smallidx = res.index(big)+1, res.index(small)+1
        return arr[bigidx] - small if flag == 0 else arr[smallidx] - big
        
            
            
        