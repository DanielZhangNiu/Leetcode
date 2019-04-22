"""
    Implement a basic calculator to evaluate a simple expression string.
    
    The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
    
    Example 1:
    
    Input: "1 + 1"
    Output: 2
    Example 2:
    
    Input: " 2-1 + 2 "
    Output: 3
    Example 3:
    
    Input: "(1+(4+5+2)-3)+(6+8)"
    Output: 23
    Note:
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.

"""
    def calculate(s: 'str') -> 'int':
        
    """
    众所周知，实现计算器需要使用一个栈，来保存之前的结果，把后面的结果计算出来之后，和栈里的数字进行操作。
    使用了res表示不包括栈里数字在内的结果，num表示当前操作的数字，sign表示运算符的正负，用栈保存遇到括号时前面计算好了的结果和运算符。
            
    操作的步骤是：
            
    1. 如果当前是数字，那么更新计算当前数字；
    2. 如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，并把当前数字num设为0，sign设为正负，重新开始；
    3. 如果当前是(，那么说明后面的小括号里的内容需要优先计算，所以要把res，sign进栈，更新res和sign为新的开始；
    4. 如果当前是)，那么说明当前括号里的内容已经计算完毕，所以要把之前的结果出栈，然后计算整个式子的结果；
    最后，当所有数字结束的时候，需要把结果进行计算，确保结果是正确的。
    """
    if not s: return 0
    res, num , sign = [], 0 ,"+"
        
    def update(sign, num):
        if sign == "+":
            res.append(num)
        elif sign == "-":
            res.append(-num)

    for ch in s:
        if ch.isdigit():
            num = 10 * num + int(ch)
        elif ch == '(':
            res.append(sign)
            num = 0
            sign = '+'
            
        elif ch in ['+', '-',')']:
            update(sign, num)
            if ch == ')':
                num = 0
                while isinstance(res[-1],int):
                    num += res.pop()
                sign = res.pop()
                update(sign, num)
            sign = ch
            num = 0

    # last ch is digit, so do the last calculation based on last sign
    update(sign, num)
    return sum(res)



