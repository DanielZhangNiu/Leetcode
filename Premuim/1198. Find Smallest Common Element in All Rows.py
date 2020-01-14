"""
 Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

 If there is no common element, return -1.

  

 Example 1:

 Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
 Output: 5
  

 Constraints:

 1 <= mat.length, mat[i].length <= 500
 1 <= mat[i][j] <= 10^4
 mat[i] is sorted in increasing order.
"""

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        cnt = collections.Counter(mat[0])
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] in cnt:
                    cnt[mat[i][j]] += 1
        res = [i for i,v in cnt.items() if v == len(mat)]
        
        return min(res) if res else -1
