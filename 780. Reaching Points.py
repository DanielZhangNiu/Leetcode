"""
    A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
    
    Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
    
    Examples:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)
    
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False
    
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True
    
    Note:
    
    sx, sy, tx, ty will all be integers in the range [1, 10^9].

"""

def reachingPoints(sx, sy, tx, ty):
    """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        
我们的目标是将tx和ty分别缩小到sx和sy，不可能一步就缩小到位，那么这肯定是一个循环，终止条件是tx和ty中任意一个小于了sx和sy，那么在循环内部，我们想要缩小tx或ty，先缩小两者中较大的那个，若tx大于ty，我们可以尝试缩小tx，但是如果此时ty等于sy了话，我们可以迅速判断出结果，通过计算此时tx和sx的差值是否是ty的倍数，因为此时ty不能改变了，只能缩小tx，若能通过减去整数倍数个ty得到sx的，就表示可以到达。如果ty不等于sy的话，那么直接tx对ty取余即可。同理，若ty大于tx，我们可以尝试缩小ty，但是如果此时tx等于sx了话，我们可以迅速判断出结果，通过计算此时ty和sy的差值是否是tx的倍数，如果tx不等于sx的话，那么直接ty对tx取余即可。循环退出后检测起始点和目标点是否相等，参见代码如下：
        
        
        if tx < ty:
            return self.dfs(sx, sy, tx, ty)
        else:
            return self.dfs(sy, sx, ty, tx)
        
        def dfs(self, sx,sy,tx,ty):
        if tx < sx:
            return False
        elif tx == sx:
            if ty < sy: return False
            return ((ty - sy) % sx) == 0
        else:
            return self.dfs(sy, sx, ty % tx, tx)
        
        """
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty == sy:
                    return (tx - sx) % ty == 0
                else:
                    tx %= ty
            else:
                if tx == sx:
                    return (ty - sy) % tx == 0
                else:
                    ty %= tx

        return tx == sx and ty == sy
