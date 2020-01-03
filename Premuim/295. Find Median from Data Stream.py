"""
 Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

 For example,
 [2,3,4], the median is 3

 [2,3], the median is (2 + 3) / 2 = 2.5

 Design a data structure that supports the following two operations:

 void addNum(int num) - Add a integer number from the data stream to the data structure.
 double findMedian() - Return the median of all elements so far.
  

 Example:

 addNum(1)
 addNum(2)
 findMedian() -> 1.5
 addNum(3)
 findMedian() -> 2
  

 Follow up:

 If all integer numbers from the stream are between 0 and 100, how would you optimize it?
 If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""
class MedianFinder:
    """
Max-heap small has the smaller half of the numbers.
Min-heap large has the larger half of the numbers.
This gives us direct access to the one or two middle values (they're the tops of the heaps), so getting the median takes O(1) time. And adding a number takes O(log n) time.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_left_heap = [] #has the smaller half of the numbers.
        self.min_right_heap = [] #has the larger half of the numbers

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.min_right_heap or num >= self.min_right_heap[0]:
            heapq.heappush(self.min_right_heap, num)
        else:
            heapq.heappush(self.max_left_heap, -num)
            
        self.balance()
        
    def balance(self):
        diff = len(self.max_left_heap) - len(self.min_right_heap)
        if diff > 1:
            heapq.heappush(self.min_right_heap, -heapq.heappop(self.max_left_heap))
        elif diff < -1:
            heapq.heappush(self.max_left_heap, -heapq.heappop(self.min_right_heap))
            
        
    def findMedian(self):
        """
        :rtype: float
        """
        diff = len(self.max_left_heap) - len(self.min_right_heap)
        if diff > 0:
            return -self.max_left_heap[0]
        elif diff < 0:
            return self.min_right_heap[0]
        else:
            return (self.min_right_heap[0] - self.max_left_heap[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
