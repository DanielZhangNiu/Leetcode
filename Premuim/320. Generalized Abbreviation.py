"""
 Write a function to generate the generalized abbreviations of a word.

 Note: The order of the output does not matter.

 Example:

 Input: "word"
 Output:
 ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def dfs(cur, pos, count):
            if pos == len(word):
                res.append((cur + str(count)) if count else cur)
            else:
                dfs(cur, pos + 1, count + 1)
                dfs(cur + (str(count) if count else '') + word[pos], pos + 1, 0)
                
        res = []
        dfs('', 0, 0)
        return res
