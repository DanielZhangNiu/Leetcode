
"""
    Given an array of strings, group anagrams together.
    
    Example:
    
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    Note:
    
    All inputs will be in lowercase.
    The order of your output does not matter.
"""
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
            
    if not strs:
        return []
    
    hashtable = {}
    res = []
    for ch in strs:
        tmp = str(sorted(ch))
        if tmp in hashtable:
            hashtable[tmp].append(ch)
        else:
            hashtable[tmp] = ch

    res = [i for i in hashtable.values()]
    return res

