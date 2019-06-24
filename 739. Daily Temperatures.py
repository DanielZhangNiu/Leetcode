"""
    Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
    
    For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
    
    Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
    


"""
def dailyTemperatures(temperatures):
    if not temperatures: return []
    res = [0] * len(temperatures)
    stack = []
    for cur_idx, cur_val in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < cur_val:
            pre = stack.pop()
            res[pre] = cur_idx - pre
        stack.append(cur_idx)
    return res

