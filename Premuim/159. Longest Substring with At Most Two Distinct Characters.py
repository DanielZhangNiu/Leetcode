"""
 Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

 Example 1:

 Input: "eceba"
 Output: 3
 Explanation: t is "ece" which its length is 3.
 Example 2:

 Input: "ccaabbb"
 Output: 5
 Explanation: t is "aabbb" which its length is 5.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s: return 0
        res = j = 0
        cnt = collections.defaultdict(int)
        for i in range(len(s)):
            cnt[s[i]] += 1
            while j < len(s) and len(cnt) > 2:
                cnt[s[j]] -= 1
                if cnt[s[j]] == 0:
                    cnt.pop(s[j])
                j += 1
            res = max(res, i - j + 1)
        
        return res
