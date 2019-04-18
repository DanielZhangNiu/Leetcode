"""
    Given a string, find the length of the longest substring without repeating characters.
    
    Example 1:
    
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:
    
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:
    
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    res = collections.defaultdict(lambda:0)
    cnt = j = 0
    for i in range(len(s)):
        while j < len(s) and res[s[j]] == 0:
            res[s[j]]+=1
            cnt = max(cnt,j-i+1)
            j+=1
                                
        res[s[i]] -= 1
    return cnt

