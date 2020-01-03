"""
 Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

 Example:
 Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

 Input: word1 = “coding”, word2 = “practice”
 Output: 3
 Input: word1 = "makes", word2 = "coding"
 Output: 1
 Note:
 You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
class WordDistance:

    def __init__(self, words: List[str]):
        self.length = len(words)
        self.table = collections.defaultdict(list)
        for i, val in enumerate(words):
            self.table[val].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        
        l1 , l2 = self.table[word1],self.table[word2]
        res = self.length
        ptr1, ptr2 = 0 , 0
    
        # O(m+n) time complexity
        while ptr1 < len(l1) and ptr2 < len(l2):
            res = min(res, abs( l1[ptr1] - l2[ptr2]))
            if l1[ptr1] < l2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
