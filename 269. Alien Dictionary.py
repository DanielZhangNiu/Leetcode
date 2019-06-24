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
def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if not words: return ""
    edgemap = {}
    letters = [0 for _ in range(26)]
    for word in words:
        for ch in word:
            key = ord(ch) - ord('a')
            edgemap[key] = []

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        for j in range(min(len(word1),len(word2))):
            key1 = ord(word1[j]) - ord('a')
            key2 = ord(word2[j]) - ord('a')
            if key1 != key2:
                if key2 not in edgemap[key1]:
                    letters[key2] += 1
                    edgemap[key1].append(key2)
                break

    availables = [ i for i, v in enumerate(letters) if i in edgemap and v == 0]
    res = ""
    where availables:
        cur = availables.pop(0)
        res += chr(cur + ord('a'))
        for greater in edgemap[cur]:
            letters[greater] -= 1
            if not letters[greater] :
                availables.insert(0,greater)

    return res if len(edgemap) == len(res) else ""



