
"""
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
    
    Example 1:
    
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    Example 2:
    
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false

"""
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    # BFS
    """
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    queue, visited = [(0, 0)], set((0, 0))
    while queue:
    x, y = queue.pop(0)
    if x+y == l:
        return True
    if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
        queue.append((x+1, y));
        visited.add((x+1, y))
    if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
        queue.append((x, y+1));
        visited.add((x, y+1))
    
    return False
    """
    """
        
    Ø d b b c a
  Ø T F F F F F
  a T F F F F F
  a T T T T T F
  b F T T F T F
  c F F T T T T
  c F F F T F T
首先，这道题的大前提是字符串s1和s2的长度和必须等于s3的长度，如果不等于，肯定返回false。
那么当s1和s2是空串的时候，s3必然是空串，则返回true。所以直接给dp[0[0]赋值true，然后若s1和s2其中的一个为空串的话，那么另一个肯定和s3的长度相等，则按位比较，若相同且上一个位置为True，赋True，其余情况都赋False，这样的二维数组dp的边缘就初始化好了。
下面只需要找出递推公式来更新整个数组即可，我们发现，在任意非边缘位置dp[i][j]时，它的左边或上边有可能为True或是False，两边都可以更新过来，只要有一条路通着，那么这个点就可以为True。那么我们得分别来看，如果左边的为True，那么我们去除当前对应的s2中的字符串s2[j - 1] 和 s3中对应的位置的字符相比（计算对应位置时还要考虑已匹配的s1中的字符），为s3[j - 1 + i], 如果相等，则赋True，反之赋False。 而上边为True的情况也类似，所以可以求出递推公式为：
        
dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);
        
        
其中dp[i][j] 表示的是 s2 的前 i 个字符和 s1 的前 j 个字符是否匹配 s3 的前 i+j 个字符，根据以上分析，可写出代码如下：
"""
    if s1 == '':
        return s2 == s3

    if s2 == '':
        return s1 == s3

    if s3 == '':
        return s1 == s2 == ''

    len1, len2, len3 = len(s1), len(s2), len(s3)
    if len3 != len1 + len2:
        return False

    dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = True

    for i in range(1, len1 + 1):
        dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]


    for j in range(1, len2 + 1):
        dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            dp[i][j] = (dp[i - 1][j] and s3[i - 1 + j] == s1[i - 1]) or (dp[i][j - 1] and s3[i - 1 + j] == s2[j - 1])

    return dp[-1][-1]

