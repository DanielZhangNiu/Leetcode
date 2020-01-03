"""
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 Example 1:

 Input:  "69"
 Output: true
 Example 2:

 Input:  "88"
 Output: true
 Example 3:

 Input:  "962"
 Output: false
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num: return True
        table = {'6':'9','9':'6'}
        res = []
        for i in num:
            if i in '69':
                res.append(table[i])
            elif i in '018':
                res.append(i)
            else:
                return False
        ans = ''.join(res)
        return ans[::-1] == num
    
