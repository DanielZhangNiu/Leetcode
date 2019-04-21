
"""
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    
    Example:
    
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    Note:
    
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections
def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not s or not t: return ""
        if len(s) < len(t): return ""
        
        t_dict = collections.Counter(t)
        start, fast, counter = 0, 0, len(t)
        idx = 0
        minlen = sys.maxsize
        
        while fast < len(s):
            if t_dict[s[fast]] > 0:   # if s[fast] is valid char in dict
                counter -= 1           # count -1 means we found 1 vaild element
                t_dict[s[fast]] -= 1
                
                while counter == 0:   # all matche at this moment
                    if fast - start < minlen:
                        minlen = fast - start + 1
                        idx = start
                    # if the leftmost element we will delete is in T and only
                    if t_dict[s[start]] == 0:
                        # which means after move start, string no longer matching, one more char need
                        counter += 1
                    #一开始，只有abc是1，其他都是0，travse的时候abc会减成0，b是-1因为出现两次，其他都会减成-2不用管，所以减掉第一个b没问题因为b是0，就不满足条件： if t_dict[s[fast]] > 0
                    t_dict[s[start]] += 1
                    start += 1
            else:
                t_dict[s[fast]] -= 1
            
            fast += 1
    
    return "" if minlen == sys.maxsize else s[idx:idx + minlen]


