"""
 Implement a basic calculator to evaluate a simple expression string.

 The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

 The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

 You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

 Some examples:

 "1 + 1" = 2
 " 6-4 / 2 " = 4
 "2*(5+5*2)/3+(6/2+8)" = 21
 "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
  

 Note: Do not use the eval built-in library function.

"""
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        res, num , sign = [], 0 ,"+"
        
        def update(sign, num):
            if sign == "+":
                res.append(num)
            elif sign == "-":
                res.append(-num)
            elif sign == '*':
                res.append(num * res.pop())
            elif sign == '/':
                res.append(int(res.pop()/num))
            elif sign == '^':
                res.append(res.pop()**num)
                
        
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == '(':
                res.append(sign)
                num = 0
                sign = '+'
            
            elif ch in '+-*/)':
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
        
