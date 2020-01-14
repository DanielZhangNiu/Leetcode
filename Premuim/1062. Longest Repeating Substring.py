"""
 Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

  

 Example 1:

 Input: "abcd"
 Output: 0
 Explanation: There is no repeating substring.
 Example 2:

 Input: "abbaba"
 Output: 2
 Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
 Example 3:

 Input: "aabcaabdaab"
 Output: 3
 Explanation: The longest repeating substring is "aab", which occurs 3 times.
 Example 4:

 Input: "aaaaa"
 Output: 4
 Explanation: The longest repeating substring is "aaaa", which occurs twice.
  

 Note:

 The string S consists of only lowercase English letters from 'a' - 'z'.
 1 <= S.length <= 1500

"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        if not S: return 0
        """
        table = collections.defaultdict(int)
        for i in range(len(S)):
            for j in range(i+1, len(S)):
                table[str(S[i:j+1])] += 1
        
        res = 0
        for sub, cnt in table.items():
            res = max(len(sub),res) if cnt > 1 else res
        return res if res > 1 else 0
            a b b a b a
        a     0 0 1 0 1
        b       1 0 2 0
        b         0 1 0
        a           0 2
        b             0
        a
        
        """
        res = 0
        dp = [[0 for i in range(len(S)+1)] for j in range (len(S)+1)]
        for i in range(1, len(S)+1):
            for j in range(i+1, len(S)+1):
                if S[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        res = max([max(i) for i in dp])
        
        return res
                
