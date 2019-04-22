"""
    Given two strings s and t , write a function to determine if t is an anagram of s.
    
    Example 1:
    
    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:
    
    Input: s = "rat", t = "car"
    Output: false
    Note:
    You may assume the string contains only lowercase alphabets.
    
    Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import collections
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
        
    if len(s)!=len(t):
        return False
        
    return False if ''.join(sorted(s)) != ''.join(sorted(t)) else True

    """
    if len(s)!=len(t):
    return False

    cnts = collections.Counter(s)
    cntt = collections.Counter(t)
    return cnts == cntt
