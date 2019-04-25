"""
    Given a pattern and a string str, find if str follows the same pattern.
    
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
    
    Example 1:
    
    Input: pattern = "abab", str = "redblueredblue"
    Output: true
    Example 2:
    
    Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
    Output: true
    Example 3:
    
    Input: pattern = "aabb", str = "xyzabcxzyabc"
    Output: false
    Notes:
    You may assume both pattern and str contains only lowercase letters.

"""
def wordPatternMatch(pattern: 'str', str: 'str') -> 'bool':
    
    pDict = dict()
    sDict = set()
    return helper(pattern, str, pDict, sDict)
    
    
    """
        start with one char to one char, like {a:r,b:e}, next 'a' coming but next str is 'd', so return false,
        and extend b:ed, continue check, until the whole traversal, return to a: re, and keep iterating until we
        found that a:red, b:blue
        """
def helper(pattern, str, pDict, sDict):
    if len(pattern) == 0 and len(str) == 0:
        return True
    elif len(pattern) ==0 or len(str) == 0:
        return False
        
    c = pattern[0]
    if c in pDict:
        word = pDict[c]
        n = len(word)
        if len(str) < n or str[:n] != word:
            return False
        else:
            return self.helper(pattern[1:], str[n:], pDict, sDict)
    else:
        # backtracing
        for i in range(1, len(str) + 1):
            word = str[:i]
            if word not in sDict:
                pDict[c] = word
                sDict.add(word)
                if self.helper(pattern[1:], str[i:], pDict, sDict):
                    return True
                pDict.pop(c)
                sDict.remove(word)
        return False
