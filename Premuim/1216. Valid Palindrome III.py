"""
 Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

 A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

  

 Example 1:

 Input: s = "abcdeca", k = 2
 Output: true
 Explanation: Remove 'b' and 'e' characters.
  

 Constraints:

 1 <= s.length <= 1000
 s has only lowercase English letters.
 1 <= k <= s.length


"""

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Just need to check how many char we need to change the s to be reversed s!!
        same with edit distance or 583 delete operations for two strings
        """
        if len(s) <= k: return True
        cnt = collections.Counter(s)
        odd = 0
        for i , v in cnt.items():
            if v % 2 != 0:
                odd += 1
                if odd - k > 1: return False
                
        rs = s[::-1]
        dp = [[0 for j in range(len(s) + 1 )] for i in range(len(s) + 1)]
        for i in range(len(s) + 1 ):
            dp[i][0] = i
        for j in range(len(s) + 1):
            dp[0][j] = j
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i-1] == rs[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1] <= 2 * k
            
   
