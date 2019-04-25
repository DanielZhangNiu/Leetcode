"""
    Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
    
    Example 1:
    
    Input: [1,2,3,4,5], k=4, x=3
    Output: [1,2,3,4]
    Example 2:
    
    Input: [1,2,3,4,5], k=4, x=-1
    Output: [1,2,3,4]
    Note:
    
    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104

"""
def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]

        
    """
    """
    Basic idea is using bisect_left find the idx(or provided idx) in the arr, the candidates for closes k would only be in left k and right k elements of this idx. Then just simple do a two pointer to find right index range.
    """
    idx = self.bisect_left(arr, x)  # find the index of x
        
    left, right = max(0, idx - k), min(idx + k, len(arr) - 1)
    #O(k)
    while right - left + 1 > k: #more than k element in the range
        if x - arr[left] > arr[right] - x: #remove left candidates, right one is closer to x
            left += 1
        else:                   # remove right condidates
            right -= 1
    return arr[left: right + 1]
    
def bisect_left(arr, target):
    l , r = 0 , len(arr) - 1
    while l <= r:
        mid = (l + r )//2
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l


    """
    这道题给我们了一个数组，还有两个变量k和x。让我们找数组中离x最近的k个元素，而且说明了数组是有序的，如果两个数字距离x相等的话，取较小的那个。从给定的例子可以分析出x不一定是数组中的数字，我们想，由于数组是有序的，所以最后返回的k个元素也一定是有序的，那么其实就是返回了原数组的一个长度为k的子数组，转化一下，实际上相当于在长度为n的数组中去掉n-k个数字，而且去掉的顺序肯定是从两头开始去，因为距离x最远的数字肯定在首尾出现。那么问题就变的明朗了，我们每次比较首尾两个数字跟x的距离，将距离大的那个数字删除，直到剩余的数组长度为k为止，参见代码如下：
        """
    res = collections.deque(arr)
    
    while len(res) > k:
        if abs(x - res[0]) <= abs(x - res[-1]):
            res.pop()
        else:
            res.popleft()

return list(res)


