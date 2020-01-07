"""
    Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

    A string such as "word" contains only the following valid abbreviations:

    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
    Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

    Note:
    Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

    Example 1:

    Given s = "internationalization", abbr = "i12iz4n":

    Return true.
    Example 2:

    Given s = "apple", abbr = "a2e":

    Return false.
"""
class Solution:
  def validWordAbbreviation(self, word, abbr):
      """
      :type word: str
      :type abbr: str
      :rtype: bool
      """
      if not word and not abbr:
          return True
      if not word or not abbr:
          return False
      l, r = 0, 0
      while l < len(abbr) and r < len(word):
          if abbr[l] >= 'a':
              if abbr[l] != word[r]:
                  return False
              l+=1
              r+=1
          else:
              if abbr[l] == '0':
                      return False
              tmp = ''
              while l < len(abbr) and abbr[l] < 'a' :
                  tmp += abbr[l]
                  l+=1
              r += int(tmp)
      
      return True if l == len(abbr) and r == len(word) else False
  
  
"""
    class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isnumeric():
                if abbr[j] == '0':
                    return False
                jprev = j
                while j < len(abbr) and abbr[j].isnumeric():
                    j += 1
                i += int(abbr[jprev:j])
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == len(word) and j == len(abbr)
"""

