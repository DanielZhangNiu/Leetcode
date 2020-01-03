"""
 Given a string, determine if a permutation of the string could form a palindrome.

    Example 1:

    Input: "code"
    Output: false
    Example 2:

    Input: "aab"
    Output: true
    Example 3:

    Input: "carerac"
    Output: true
    Accepted
    76,465
    Submissions
    125,603
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s: return True
        cnt = collections.Counter(s)
        odd = 0
        for key,val in cnt.items():
            if val % 2 == 1:
                odd += 1
                if odd > 1: return False
        return True
