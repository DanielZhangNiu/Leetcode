"""
 We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

 A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

 Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

  

 Example 1:

 Input: 20
 Output: 6
 Explanation:
 The confusing numbers are [6,9,10,16,18,19].
 6 converts to 9.
 9 converts to 6.
 10 converts to 01 which is just 1.
 16 converts to 91.
 18 converts to 81.
 19 converts to 61.
 Example 2:

 Input: 100
 Output: 19
 Explanation:
 The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
  

 Note:

 1 <= N <= 10^9
"""
class Solution:
    def confusingNumberII(self, N: int) -> int:
        nums = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        def find_total(n):
            """
            The total count of numbers formed by the "confusing" digits

            """
            if not n:
                return 1
            # the total count of numbers with the same number of digits as the
            # given `n` and led by confusing digits smaller than the one in `n`.
            # Since there are five options for every digit after the leading
            # one, there are a total of `5^(len(n) - 1)` variations for each
            # qualified leading digit
            total = sum(n[0] > nn for nn in nums) * 5 ** (len(n) - 1)
            # in case the leading digit of `n` is confusing
            if n[0] in nums:
                # count the number of numbers composed of confusing digits led
                # by this digit
                total += find_total(n[1:])
            return total
        
        
        def find_strobogrammatic(arr, l, r):
            """
            Count the total of strobogrammatic numbers by forming them from both
            ends simultaneously
            """
            res = 0
            # when the left and right pointers meet, a strobogrammatic number is
            # formed
            if l > r:
                n = ''.join(arr)
                # it only counts if smaller than the given `N`
                if int(n) < N:
                    res += 1
            # before they meet
            else:
                # go over the confusing digit pairs
                for k, v in nums.items():
                    # add them to both ends
                    arr[l], arr[r] = k, v
                    # two cases need to be skipped:
                    # 1) a number greater than 9 has a leading zero
                    # 2) left and right pointers point to the same position but
                    #    different values
                    if (len(arr) > 1 and arr[0] == '0') or (l == r and k != v):
                        continue
                    # move the left and right pointers and find strobogrammatic
                    # numbers recursively
                    res += find_strobogrammatic(arr, l + 1, r - 1)
            return res
        
        n_str = str(N)
        # count the total of numbers formed by the confusing digits
        total = find_total(n_str)
        # find the strobogrammatic numbers with different number of digits, and
        # subtract the count from the total
        for l in range(1, len(n_str) + 1):
            total -= find_strobogrammatic([0] * l, 0, l - 1)
        return total
