"""
 Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

 Example 1:

 Input: "aabb"
 Output: ["abba", "baab"]
 Example 2:

 Input: "abc"
 Output: []

"""
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if not s: return []
    
        # make first half palindrome
        dic = collections.Counter(s)
        half = []
        self.mid = ""
        odd = 0
        for k, v in dic.items():  #a :2, b :2
            half += k * (v // 2)  # half = a *1 + b*1
            if v % 2 == 1:
                self.mid = k  # the very center char, only 1
                odd += 1
            
            if odd > 1: return [] # odd > 1 cannot be palindrome

        # find all permutations
        res = []
        visited = [0] * len(half)
        self.backtrace(visited, half ,"", res,0)
        return res

    def backtrace(self, visited, half, path, res,idx):
    
        if len(path) == len(half):
            res.append(path + self.mid + path[::-1])
            return

        for i in range(idx,len(half)):
        
            if i > 0 and visited[i-1] == 0 and half[i] == half[i-1]:
                continue
            if visited[i] == 0:
                visited[i] = 1
                self.backtrace(visited, half, path + half[i], res,idx)
                visited[i] = 0
