"""
    Given two strings s and t, determine if they are both one edit distance apart.
    
    Note:
    
    There are 3 possiblities to satisify one edit distance apart:
    
    Insert a character into s to get t
    Delete a character from s to get t
    Replace a character of s to get t
    Example 1:
    
    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.
    Example 2:
    
    Input: s = "cab", t = "ad"
    Output: false
    Explanation: We cannot get t from s by only one step.
    Example 3:
    
    Input: s = "1203", t = "1213"
    Output: true
    Explanation: We can replace '0' with '1' to get t.

"""
def isOneEditDistance(s: 'str', t: 'str') -> 'bool':
    if s == t:
        return False
    ls, lt = len(s), len(t)
    if ls > lt: # force s shorter than t
        return self.isOneEditDistance(t, s)
    if lt - ls > 1:
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            if ls == lt:
                s = s[:i]+t[i]+s[i+1:]  # replacement
            else:
                s = s[:i]+t[i]+s[i:]  # insertion
            break
    return s == t or s == t[:-1]


