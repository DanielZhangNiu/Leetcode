"""
 Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

 Begin with the first character and then the number of characters abbreviated, which followed by the last character.
 If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
 If the abbreviation doesn't make the word shorter, then keep it as original.
 Example:

 Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
 Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
 Note:
 Both n and the length of each word will not exceed 400.
 The length of each word is greater than 1.
 The words consist of lowercase English letters only.
 The return answers should be in the same order as the original array.
"""
class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        if not dict: return []
        res = [0] * len(dict)
        prefix = [1] * len(dict)
        count = collections.defaultdict(lambda:0)
        
        for i in range(len(dict)):
            res[i] = self.getAbbr(dict[i],1)
            #if res[i] not in count:
            #   count[res[i]] = 0
            count[res[i]] += 1
            
        while True:
            unique = True
            for i in range(len(dict)):
                if count[res[i]] > 1:
                    prefix[i]+=1
                    res[i] = self.getAbbr(dict[i],prefix[i])
                     #if res[i] not in count:
                    #   count[res[i]] = 0
                    count[res[i]] += 1
                    unique = False
            if unique:
                break
        return res
        
    def getAbbr(self,s, p):
        if p >= len(s) - 2:
            return s
        
        ans = ""
        ans = s[:p] + str(len(s)-1-p) +s[-1]
        return ans
