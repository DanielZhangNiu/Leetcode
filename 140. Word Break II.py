"""
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
    
    Note:
    
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    Example 1:
    
    Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
    "cats and dog",
    "cat sand dog"
    ]
    Example 2:
    
    Input:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.
    Example 3:
    
    Input:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output:
    []
"""
def wordBreak(s, dict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = []

    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)+1):
        if dp[i] == False:
            continue
        for j in range(i, len(s)):
            if s[i:j+1] in dict:
                dp[j+1] = True
    return backtrace(s,dp,dict)

#use backtracing to compose the result
def backtrace(s, dp, dict):
    res = []
    for i in range(len(s)-1, -1, -1):
        if dp[i] == False:
            continue
        if s[i:] in dict:
            if i == 0:
                res += s
        for output in backtrace(s[:i],dp, dict):
            res += [output+ " "+ s[i:]]
    return res

