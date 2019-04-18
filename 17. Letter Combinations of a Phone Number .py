"""
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    
    
    Example:
    
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    Note:
    
    Although the above answer is in lexicographical order, your answer could be in any order you want.
    
"""
def letterCombinations(digits):
    """
        :type digits: str
        :rtype: List[str]
    """
    if len(digits) == 0: return []
    self.map = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}
                    
    self.res = []
    self.dfs(digits, "",0)
    return self.res

def dfs(digits,path,idx):
    
    if len(path) > len(digits):
        return
    if len(path) == len(digits):
        self.res.append(path)
    for i in range(idx,len(digits)):
        for char in self.map[digits[i]]:
            self.dfs(digits,path+char,i+1)
