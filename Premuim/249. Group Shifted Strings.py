"""
 Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

 "abc" -> "bcd" -> ... -> "xyz"
 Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

 Example:

 Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
 Output:
 [
   ["abc","bcd","xyz"],
   ["az","ba"],
   ["acef"],
   ["a","z"]
 ]
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings: return []
    
        groups = collections.defaultdict(list)
        for word in strings:
            tmp = ""
            for ch in word:
                tmp += str((ord(ch) - ord(word[0]))%26) + " "
            groups[tmp].append(word)
    
        return [val for idx,val in groups.items()]
