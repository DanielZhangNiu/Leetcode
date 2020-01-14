"""
 Given a year Y and a month M, return how many days there are in that month.

  

 Example 1:

 Input: Y = 1992, M = 7
 Output: 31
 Example 2:

 Input: Y = 2000, M = 2
 Output: 29
 Example 3:

 Input: Y = 1900, M = 2
 Output: 28
  

 Note:

 1583 <= Y <= 2100
 1 <= M <= 12
"""
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        flag = False
        if (Y % 4==0 and Y % 100!=0) or (Y % 400 ) == 0:
            flag = True
        
        if M in (1,3,5,7,8,10,12):
            return 31
        elif M == 2 and flag:
            return 29
        elif M == 2:
            return 28
        else:
            return 30
