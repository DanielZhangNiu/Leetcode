
"""
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    
    Example 1:
    
    Input: num1 = "2", num2 = "3"
    Output: "6"
    Example 2:
    
    Input: num1 = "123", num2 = "456"
    Output: "56088"
    Note:
    
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
    
"""
def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str

    """
        
    if num1 == "0" or num2 == "0":
        return "0"
        
    num1 = list(map(int, list(num1)))
    num2 = list(map(int, list(num2)))
        
    res = [0] * (len(num1) + len(num2))
        
    for i, n1 in enumerate(num1[::-1]):
        for j, n2 in enumerate(num2[::-1]):
            res[i+j] += n1*n2
        
    carry = 0
    for k in range(len(res)):
        res[k] += carry
        carry, res[k] = res[k] // 10, res[k] % 10
        
    return "".join(map(str, res[::-1])).lstrip("0")
