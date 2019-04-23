"""
    Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
    
    Note: The input string may contain letters other than the parentheses ( and ).
    
    Example 1:
    
    Input: "()())()"
    Output: ["()()()", "(())()"]
    Example 2:
    
    Input: "(a)())()"
    Output: ["(a)()()", "(a())()"]
    Example 3:
    
    Input: ")("
    Output: [""]


"""
def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s: return []
    lc, rc = 0 , 0
    for ch in s:
        if ch == '(':
            lc += 1
        elif lc == 0:
            if ch == ')':
                rc += 1
        else:
            if ch == ')':
                lc -= 1
    res = []
    res = dfs(s, 0, lc , rc, res )
    return res

# left/right is the number of left/right parentheses to remove
def dfs(s, start,  left, right, res):
    if left == right == 0:
        if isValid(s):
            res.append(s)
            return res
    for i in range(start, len(s)):
         # only remove the first parenthrese when ther are consecutive, avoid duplication
        if i!= start and s[i] == s[i-1]: continue
        if s[i] == '(' or s[i] == ')':
            cur_str = s[i:]+s[i+1:] # remove s[i], dfs the rest of string
            if right > 0:
                dfs(cur_str, i, left, right -1)
            elif left > 0:
                dfs(cur_str, i, left-1, right)

def isValid(substr):
    cnt = 0
    for ch in substr:
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
        if cnt < 0 : return False
    return cnt == 0

