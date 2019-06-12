"""
    A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
    
    Example 1:
    
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    Note:
    
    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.


"""
def partitionLabels(S: str) -> List[int]:
    if not S: return []
    res = []
    dict = collections.defaultdict(lambda:0)
    for i, v in S:
        dict[v] = i

    l, r = 0, 0
    for i,c in enumerate(S):
        r = max(r, dict[c])
        if i == r:
            res.append(r - l + 1)
            l = r + 1
    return res






