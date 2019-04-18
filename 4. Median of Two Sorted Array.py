"""
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    
    You may assume nums1 and nums2 cannot be both empty.
    
    Example 1:
    
    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0
    Example 2:
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5
    
"""
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
        
    原问题难以直接递归求解，所以我们先考虑这样一个问题：
    在两个有序数组中，找出第k大数。
        
    如果该问题可以解决，那么第 (n + m) / 2 大数就是我们要求的中位数.
    先从简单情况入手，假设 m, n >= k/2，我们先从 nums1 和 nums2 中各取前 k/2 个元素：
    如果 nums1[k/2-1] > nums2[k/2-1]，则说明 nums1 中取的元素过多，nums 中取的元素过少；
    因此 nums2 中的前 k/2 个元素一定都小于等于第 k 大数，所以我们可以先取出这些数，将问题归约成在剩下的数中找第 k - [ k/2 ] 大数.
    如果 nums1[k/2-1] <= nums2[k/2-1]，同理可说明 nums1 中的前 k/2 个元素一定都小于等于第 k 大数，类似可将问题的规模减少一半.
    现在考虑边界情况，如果 m < k/2，则我们从 nums1 中取m个元素，从nums2 中取 k/2 个元素（由于 k = (n + m) / 2，因此 m,n 不可能同时小于 k/2.）：
        
    如果 nums1[m-1] > nums2[k/2-1]，则 nums2 中的前 k/2 个元素一定都小于等于第 k 大数，我们可以将问题归约成在剩下的数中找第 k - [k/2] 大数.
    如果 nums1[m-1] <= nums2[k/2-1]，则 nums1 中的所有元素一定都小于等于第 k 大数，因此第k大数是 nums2[k - m - 1]
        时间复杂度分析：k = (m + n) / 2，且每次递归 k 的规模都减少一半，因此时间复杂度是 O(log(m + n)).
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2.0

def kth(a, b, k):   # a = [1,3], b = [2], k = 1
    if not a:
        return b[k]
    if not b:
            return a[k]
    ia, ib = len(a) // 2 , len(b) // 2  # 1 ， 0
        ma, mb = a[ia], b[ib]  # 3， 2
        
        # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)

    # when k is smaller than the sum of a and b's indices
    else:
    # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)    #a[:ia] = [1]
        else:
            return self.kth(a, b[:ib], k)
