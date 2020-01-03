"""
 Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

 word1 and word2 may be the same and they represent two individual words in the list.

 Example:
 Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

 Input: word1 = “makes”, word2 = “coding”
 Output: 1
 Input: word1 = "makes", word2 = "makes"
 Output: 3
 Note:
 You may assume word1 and word2 are both in the list.
"""
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = len(words), len(words)
        res = len(words)
        sameflag = word1 == word2
    
        for i, v in enumerate(words):
            if v == word1:
                idx1 = i
                res = min(res, abs(idx1 - idx2))
                if sameflag:
                    idx2 = idx1
            elif v == word2 and not sameflag:
                idx2 = i
                res = min(res, abs(idx1 - idx2))
    
    return res
