"""
    Implement a basic calculator to evaluate a simple expression string.
    
    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
    
    Example 1:
    
    Input: "3+2*2"
    Output: 7
    Example 2:
    s
    Input: " 3/2 "
    Output: 1
    Example 3:
    
    Input: " 3+5 / 2 "
    Output: 5
    Note:
    
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.


"""
    def calculate(s: 'str') -> 'int':
        if not s: return 0
        res, num , sign = [], 0 ,"+"
        
        def update(sign, num):
            if sign == "+":
                res.append(num)
            elif sign == "-":
                res.append(-num)
            elif sign == "*":
                res.append(num*res.pop())
            elif sign == "/":
                res.append(int(res.pop()/num))
        
        
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch in "+-*/":
                update(sign, num)
                sign = ch
                num = 0

    # last ch is digit, so do the last calculation based on last sign
        update(sign, num)
        return sum(res)



