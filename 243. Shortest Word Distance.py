"""
    Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
    
    Example:
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Input: word1 = “coding”, word2 = “practice”
    Output: 3
    Input: word1 = "makes", word2 = "coding"
    Output: 1
    Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
def shortestDistance(words, word1, word2):
    """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1, index2 = size, size
        ans = size
                    
        for i, v in enumerate (words):
            if v == word1:
                index1 = i
                ans = min(ans, abs(index1-index2))
            elif v == word2:
                index2 = i
                ans = min(ans, abs(index1-index2))
        return ans
