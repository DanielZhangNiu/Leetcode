"""
 From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

 Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

  

 Example 1:

 Input: source = "abc", target = "abcbc"
 Output: 2
 Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
 Example 2:

 Input: source = "abc", target = "acdbc"
 Output: -1
 Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
 Example 3:

 Input: source = "xyz", target = "xzyxz"
 Output: 3
 Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
  

 Constraints:

 Both the source and target strings consist of only lowercase English letters from "a"-"z".
 The lengths of source and target string are between 1 and 1000.

"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
Example with source = "abcab", target = "aabbaac"
The inverted index data structure for this example would be:
inverted_index = {
a: [0, 3] # 'a' appears at index 0, 3 in source
b: [1, 4], # 'b' appears at index 1, 4 in source
c: [2], # 'c' appears at index 2 in source
}
Initialize i = -1 (i represents the smallest valid next offset) and loop_cnt = 1 (number of passes through source).
Iterate through the target string "aabbaac"
a => get the offsets of character 'a' which is [0, 3]. Set i to 1.
a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
b => get the offsets of character 'b' which is [1, 4]. Set i to 5.
b => get the offsets of character 'b' which is [1, 4]. Increment loop_cnt to 2, and Set i to 2.
a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
a => get the offsets of character 'a' which is [0, 3]. Increment loop_cnt to 3, and Set i to 1.
c => get the offsets of character 'c' which is [2]. Set i to 3.
We're done iterating through target so return the number of loops (3).
        """
        if not source or not target: return -1
        idx_table = collections.defaultdict(list)
        for i, val in enumerate(source):
            idx_table[val].append(i)
        res = []
        itercnt, idx = 1, 0
        for ch in target:
            if ch not in source: return -1
            curidxs = idx_table[ch]
            
            k = self.bsearch(curidxs, idx)
            if k == len(curidxs):
                itercnt += 1
                idx = curidxs[0] + 1
                res.append(idx - 1 )
            else:
                idx = curidxs[k] + 1
                res.append(idx -1)
        print(res)
        return itercnt
    
    def bsearch(self, nums, idx):
        l , r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] < idx:
                l += 1
            else:
                r -= 1
        return l
