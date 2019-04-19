"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    
    For example, given n = 3, a solution set is:
    
    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]

"""
    def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
            
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
            """
        
        if n == 0: return ['']
        res = []
        def build(path, l, r):
            if r == n:
                res.append(path)
                return
            if l < n:
                build(path + "(", l + 1, r)
            if l > r:
                build(path + ")", l, r + 1)
        
        build("", 0, 0)
        return res
