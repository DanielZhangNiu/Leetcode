"""
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    
    Example 1:
    
    Input: 121
    Output: true
    Example 2:
    
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:
    
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    Follow up:
    Coud you solve it without converting the integer to a string?

"""
def isPalindrome(self, x: int) -> bool:
    """
    :type x: int
    :rtype: bool
        
    res=str(x)
    for i in range(len(res)/2):
    if res[i]!=res[len(res)-i-1]:
    return False
    return True
        
    res = str(x)
    return True if res == res[::-1] else False
    """
            
    if x < 0:
        return False
    val = 0
    res = x
    while x:
        val = int(val * 10 + x%10)
        x = x//10
                                
    return val == res
