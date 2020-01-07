"""
 Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

 The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

 next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
 hasNext() - Judge whether there is any letter needs to be uncompressed.

 Note:
 Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

 Example:

 StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

 iterator.next(); // return 'L'
 iterator.next(); // return 'e'
 iterator.next(); // return 'e'
 iterator.next(); // return 't'
 iterator.next(); // return 'C'
 iterator.next(); // return 'o'
 iterator.next(); // return 'd'
 iterator.hasNext(); // return true
 iterator.next(); // return 'e'
 iterator.hasNext(); // return false
 iterator.next(); // return ' '
"""

class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letter = []
        for i in compressedString:
            if i.isalpha():
                self.letter.append(i)
                compressedString = compressedString.replace(i, ' ')
        #second:extract number and convert it to int from modified string
        self.number = [int(i) for i in compressedString.split()]
        
    
    def next(self):
        """
        :rtype: str
        """
        if self.number:
            if self.number[0] > 0:
                n = self.letter[0]
                self.number[0] -= 1
                if self.number[0] == 0:
                    del self.letter[0]
                    del self.number[0]
                return n
        else:
            return ' '
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.number else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
