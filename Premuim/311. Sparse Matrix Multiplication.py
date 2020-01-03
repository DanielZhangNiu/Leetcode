"""
 Given two sparse matrices A and B, return the result of AB.

 You may assume that A's column number is equal to B's row number.

 Example:

 Input:

 A = [
   [ 1, 0, 0],
   [-1, 0, 3]
 ]

 B = [
   [ 7, 0, 0 ],
   [ 0, 0, 0 ],
   [ 0, 0, 1 ]
 ]

 Output:

      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
 AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                   | 0 0 1 |

"""
class Solution:

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
       
        AB = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        if not A or not B:
            return []
        if len(A[0]) != len(B):
            return []
        
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] == 0:
                    continue
                for j in range(len(B[0])):
                    AB[i][j] += A[i][k]*B[k][j]
                    
        return AB
        """
        dictA = {}
        dictB = {}
        if len(A[0]) != len(B):
            return []
        
        # construct the hashtable for A and B
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]!=0:
                    if i not in dictA:
                        dictA[i] = {}
                    dictA[i][j] = A[i][j]

        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]!=0:
                    if j not in dictB:
                        dictB[j] = {}
                    dictB[j][i] = B[i][j]
                    
        AB = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                if i in dictA and j in dictB:
                    for k in range(len(B)):
                        if k in dictA[i] and k in dictB[j]:
                            AB[i][j] += dictA[i][k] * dictB[j][k]
                            
        return AB
