"""
 Given an input string , reverse the string word by word.

 Example:

 Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
 Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
 Note:

 A word is defined as a sequence of non-space characters.
 The input string does not contain leading or trailing spaces.
 The words are always separated by a single space.
 Follow up: Could you do it in-place without allocating extra space?
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        flag = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.helper(s,flag,i-1)
                flag = i+1
            elif i == len(s) - 1:
                self.helper(s,flag,i)
            
    def helper(self,s,left,right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
