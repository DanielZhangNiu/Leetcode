"""
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
    
    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    Note:
    
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
    Example 1:
    
    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    Output: 5
    
    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    Example 2:
    
    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    Output: 0
    
    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


"""
import collection
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    wordList = set(wordList)
    alpha = ascii_lowercase
    visited = set()
    q = collection.deque()
    q.append([beginWord,1])
    
    while q:
        cur_word, length = q.popleft()
        if cur_word == endWord:
            return length
    for i in range(len(cur_word)):
        for ch in alpha:
            new_word = cur_word[:i]+ch+cur_word[i+1:]
            if new_word in wordList and new_word not in visited:
                q.append([new_word,length+1))
                visited.add(new_word)
    return 0

