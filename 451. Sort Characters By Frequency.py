"""
    Given a string, sort it in decreasing order based on the frequency of characters.
    
    Example 1:
    
    Input:
    "tree"
    
    Output:
    "eert"
    
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    Example 2:
    
    Input:
    "cccaaa"
    
    Output:
    "cccaaa"
    
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.
    Example 3:
    
    Input:
    "Aabb"
    
    Output:
    "bbAa"
    
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

"""
import collections
def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    
    tmp=set(s)
    res=[]
    for i in tmp:
        res.append((i,s.count(i)))
    res.sort(key = lambda x: x[1], reverse = True)
        
    return ''.join(map(lambda x: x[0] * x[1], res))
        """
    count = collections.Counter(s)
    cnt = sorted(count.items(),key = lambda x : x[1], reverse = True)
    return ''.join(i[0]*i[1] for i in cnt)


