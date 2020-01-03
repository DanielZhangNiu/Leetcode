"""
 There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

 Example 1:

 Input:
 [
   "wrt",
   "wrf",
   "er",
   "ett",
   "rftt"
 ]

 Output: "wertf"
 Example 2:

 Input:
 [
   "z",
   "x"
 ]

 Output: "zx"
 Example 3:

 Input:
 [
   "z",
   "x",
   "z"
 ]

 Output: ""

 Explanation: The order is invalid, so return "".
 Note:

 You may assume all letters are in lowercase.
 You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
 If the order is invalid, return an empty string.
 There may be multiple valid order of letters, return any one of them is fine.

"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words: return ""
        graph = {}
        letters = [ 0 for i in range(26)]
        for word in words:
            for ch in word:
                key = ord(ch) - ord('a')
                graph[key] = []
    
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    key1, key2 = ord(word1[j]) - ord('a'), ord(word2[j]) - ord('a')
                    if key2 not in graph[key1]:
                        letters[key2] += 1
                        graph[key1].append(key2)
                    break
        res = ""
        availables = collections.deque([i for i,v in enumerate(letters) if i in graph and v == 0])
        while availables:
            cur = availables.popleft()
            res += chr(cur + ord('a'))
            for nxt in graph[cur]:
                letters[nxt] -= 1
                if letters[nxt] == 0:
                    availables.appendleft(nxt)
                
        return res if len(graph) == len(res) else ""  # be careful this, the res should contain very single ch from input words
                
