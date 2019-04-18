"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    
    Based on two scenarios, find a index, expand to head and tail from this center point.
    """
        
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
            
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
def helper(s, l, r):
    while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]
