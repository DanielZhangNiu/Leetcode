"""
 Given a non-negative integer num, Return its encoding string.

 The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:



  

 Example 1:

 Input: num = 23
 Output: "1000"
 Example 2:

 Input: num = 107
 Output: "101100"
  

 Constraints:

 0 <= num <= 10^9

"""
# 000, 001,010,011,100,101,110,111,0000,0001,0010,0011,0100,0101,0110,0111,1000
# convert the num + 1 into binary and drop the most significant digit
class Solution:
    def encode(self, num: int) -> str:
        if num == 0: return ""
        num += 1
        res = bin(num)[3:]
        
        return str(res)
        
        
        
