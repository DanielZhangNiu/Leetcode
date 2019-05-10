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
        dfs(s, dict, '')
        return self.res
    
#same as word break, us dp to measure whether the current s is valid or not
def check(s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            if dp[i] == False:
                continue
            for k in range(i, len(s)):
                if s[i:k+1] in dict:
                    dp[k+1] = True
        return dp[-1]

#use backtracing to compose the result
def backtrace(s, dict, stringlist):
    if check(s, dict):
        if len(s) == 0:
            self.res.append(stringlist[1:])
        for i in range(1, len(s)+1):
            if s[:i] in dict:
                backtrace(s[i:], dict, stringlist+' '+s[:i])


