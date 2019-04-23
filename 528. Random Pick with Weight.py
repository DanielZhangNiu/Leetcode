"""
    Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
    
    Note:
    
    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
    Example 1:
    
    Input:
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output: [null,0]
    Example 2:
    
    Input:
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output: [null,0,1,1,1,0]
    Explanation of Input Syntax:
    
    The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
class Solution:
    
    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        
        for i in range(1,self.n):
            w[i] += w[i-1]

    def pickIndex(self) -> int:
    
    """
    :rtype: int
        
这道题给了一个权重数组，让我们根据权重来随机取点，现在的点就不是随机等概率的选取了，而是要根据权重的不同来区别选取。比如题目中例子2，权重为 [1, 3]，表示有两个点，权重分别为1和3，那么就是说一个点的出现概率是四分之一，另一个出现的概率是四分之三。由于我们的rand()函数是等概率的随机，那么我们如何才能有权重的随机呢，我们可以使用一个trick，由于权重是1和3，相加为4，那么我们现在假设有4个点，然后随机等概率取一个点，随机到第一个点后就表示原来的第一个点，随机到后三个点就表示原来的第二个点，这样就可以保证有权重的随机啦。那么我们就可以建立权重数组的累加和数组，比如若权重数组为 [1, 3, 2] 的话，那么累加和数组为 [1, 4, 6]，整个的权重和为6，我们 rand() % 6，可以随机出范围 [0, 5] 内的数，随机到 0 则为第一个点，随机到 1，2，3 则为第二个点，随机到 4，5 则为第三个点，所以我们随机出一个数字x后，然后再累加和数组中查找第一个大于随机数x的数字，使用二分查找法可以找到第一个大于随机数x的数字的坐标，即为所求，
        """
            
        #[1,3,2]
        #after[1,4,6]
        seed = random.randint(1,self.w[-1])
        # if seed = 5
            
        l,r = 0, self.n-1
        while l<=r:
        mid = (l+r)//2
                    
            if seed > self.w[mid]:
                l = mid +1
            else:
                r = mid - 1
                                    
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

