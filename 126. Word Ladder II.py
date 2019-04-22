"""
    Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
    
    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    Note:
    
    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
    Example 1:
    
    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    Output:
    [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
    ]
    Example 2:
    
    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    Output: []
    
    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
            
    alpha = string.ascii_lowercase
                
    visited = set()
                
    wordListSet = set(wordList+[beginWord])
    graph = collections.defaultdict(list)
    q = set([beginWord])
    count = 0
    result = []
    while q:
        count +=1
        newQ = set()
        for word in q:
            wordListSet.remove(word)
        for word in q:
            if word == endWord:
                getAllPaths(graph, beginWord, endWord, result, [])
                return result
            for i in range(len(word)):
                for sub in alpha:
                    if sub != word[i]:
                        newWord = word[:i] + sub + word[i+1:]
                        if newWord in wordListSet:
                            graph[word].append(newWord)
                            newQ.add(newWord)
        q = newQ
    return []

def getAllPaths(graph, node, target, result, output):
    #This is just a backtracking pre-order traversal DFS on a DAG.
    output.append(node)
    if node==target:
        result.append(output[:])
    else:
        for child in graph[node]:
            self.getAllPaths(graph,child, target, result, output)
            output.pop()
