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
这道题给我们了一个数组，还有两个变量k和x。让我们找数组中离x最近的k个元素，而且说明了数组是有序的，如果两个数字距离x相等的话，取较小的那个。从给定的例子可以分析出x不一定是数组中的数字，我们想，由于数组是有序的，所以最后返回的k个元素也一定是有序的，那么其实就是返回了原数组的一个长度为k的子数组，转化一下，实际上相当于在长度为n的数组中去掉n-k个数字，而且去掉的顺序肯定是从两头开始去，因为距离x最远的数字肯定在首尾出现。那么问题就变的明朗了，我们每次比较首尾两个数字跟x的距离，将距离大的那个数字删除，直到剩余的数组长度为k为止，参见代码如下：
        """
    res = collections.deque(arr)
            
    while len(res) > k:
        if abs(x - res[0]) <= abs(x - res[-1]):
            res.pop()
        else:
            res.popleft()

    return list(res)

"""
    
    The array is sorted.
    If we want find the one number closest to x,
    we don't have to check one by one.
    it's straightforward to use binary research.
    
    Now we want the k closest,
    the logic should be similar.
    
    Explanation:
    
    Assume we are taking A[i] ~ A[i + k -1].
    We can binary research i
    We compare the distance between x - A[mid] and A[mid + k] - x
    
    If x - A[mid] > A[mid + k] - x,
    it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
    and we have mid smaller than the right i.
    So assign left = mid + 1.
    
    left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else :
                right = mid
                
    return arr[left: left + k]
    
    """

