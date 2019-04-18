"""
    Given a 32-bit signed integer, reverse digits of an integer.
    
    Example 1:
    
    Input: 123
    Output: 321
    Example 2:
    
    Input: -123
    Output: -321
    Example 3:
    
    Input: 120
    Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    
    res=list(str(x))[::-1]
    if res[0]==0:
        res.pop(0)
    if res[-1]=='-':
        res[0]='-'+res[0]
        res.pop(-1)
        res=int(''.join(res))
    return res if -2**31<=res<=2**31 else 0
    """
    # 123
    ## Mod 10 = 3,  divid 10 = 12
    maxInt = pow(2,31)
    flag =-1 if x < 0 else 1
    val = 0
    while 1:
        val = int(val * 10 + abs(x) % 10)
        x = int(x/10)
        if not x :
            break
    if (val > maxInt or val <= -maxInt):
        val =0
    return flag*val
