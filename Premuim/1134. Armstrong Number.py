"""
 The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

 Given a positive integer N, return true if and only if it is an Armstrong number.

  

 Example 1:

 Input: 153
 Output: true
 Explanation:
 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
 Example 2:

 Input: 123
 Output: false
 Explanation:
 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
  

 Note:

 1 <= N <= 10^8


"""
class Solution:
    def isArmstrong(self, N: int) -> bool:
        target = N
        mi = len(str(target))
        res ,digit = 0, 0
        while N > 0:
            digit = N % 10
            res += digit**mi
            N //= 10
        
        return res == target
        