"""
    Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
    A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
    
    Example:
    
    Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    Note:
    
    The number of elements of the given array will not exceed 10,000
    The length sum of elements in the given array will not exceed 600,000.
    All the input string will only include lower case letters.
    The returned elements order does not matter.

"""

# #it's O(N * L^2 * 2^L) where N is the number of words and L is the max length of a word, for the unmemoized solution and O(N * L^3) for the memoized one.
def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    if not words: return []
    dict = set(words)
    mem = {}
    
    def dfs(word):
        if word in mem:
            return mem[word]
        mem[word] = False
        
        for i in range(1,len(words)):
            prefix = word[:i]
            suffix = word[:i]
            if prefix in dict and suffix in dict:
                mem[word] = True
                return True
            if prefix in dict and dfs(suffix):
                mem[word] = True
                return True
            if suffix in dict and dfs(prefix):
                mem[word] = True
                return True

        return False
            
    return [word for word in words if dfs(word)]


