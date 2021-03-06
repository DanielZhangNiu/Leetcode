"""
 Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

   For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

   Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

   Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

   Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

   Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

   Note:

   The length of words1 and words2 will not exceed 1000.
   The length of pairs will not exceed 2000.
   The length of each pairs[i] will be 2.
   The length of each words[i] and pairs[i][j] will be in the range [1, 20].
    
"""
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """
        DFS
       
        if words1 == words2: return True
        if len(words1)!= len(words2): return False
        pairtable = collections.defaultdict(set)
        for pair in pairs:
            pairtable[pair[0]].add(pair[1])
            pairtable[pair[1]].add(pair[0])

            
        for i in range(len(words1)):
            if words1[i]!= words2[i]:
                if not self.bfs(words1[i], words2[i],pairtable):
                    return False
        return True

    def bfs(self, word1, target, table):
        Q = collections.deque([word1])
        visited = set()
        while Q:
            cur = Q.popleft()
            visited.add(cur)
            if cur == target:
                return True
            for nei in table[cur]:
                if nei not in visited:
                    Q.append(nei)
        return False
        """

        parent = {}
        
        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1!= p2:
                parent[p2] = p1
            
        for word1, word2 in pairs:
            if word1 not in parent:
                parent[word1] = word1
            if word2 not in parent:
                parent[word2] = word2
            union(word1, word2)
            
        if len(words1) != len(words2):
            return False
        
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if word1 not in parent:
                parent[word1] = word1
            if word2 not in parent:
                parent[word2] = word2
            if find(word1) != find(word2):
                return False
        return True
        
