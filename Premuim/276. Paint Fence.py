"""
 There is a fence with n posts, each post can be painted with one of the k colors.

 You have to paint all the posts such that no more than two adjacent fence posts have the same color.

 Return the total number of ways you can paint the fence.

 Note:
 n and k are non-negative integers.

 Example:

 Input: n = 3, k = 2
 Output: 6
 Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

             post1  post2  post3
  -----      -----  -----  -----
    1         c1     c1     c2
    2         c1     c2     c1
    3         c1     c2     c2
    4         c2     c1     c1
    5         c2     c1     c2
    6         c2     c2     c1

"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
    
        num_same = 0 # the number of ways that the last element has the same color as the second last one
        num_diff = k # the number of ways that the last element has differnt color from the second last one

        for i in range(1, n):
            total = num_diff + num_same
            num_same = num_diff
            num_diff = total * (k - 1)

        return num_same + num_diff
