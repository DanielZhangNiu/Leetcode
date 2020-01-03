"""
 Given a string, find the length of the longest substring T that contains at most k distinct characters.

 Example 1:

 Input: s = "eceba", k = 2
 Output: 3
 Explanation: T is "ece" which its length is 3.
 Example 2:

 Input: s = "aa", k = 1
 Output: 2
 Explanation: T is "aa" which its length is 2.
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        hashtable = collections.defaultdict(int)
        j, res = 0,0
        for i in range(len(s)):
            hashtable[s[i]]+=1
            while len(hashtable) > k:
                hashtable[s[j]]-=1
                if hashtable[s[j]]==0:
                    hashtable.pop(s[j])
                j+=1
            res = max(res,i-j+1)
        return res
