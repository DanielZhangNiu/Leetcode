"""
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
    
    Example 1:
    
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2
    Example 2:
    
    Input: [[7,10],[2,4]]
    Output: 1
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
def minMeetingRooms(intervals):
    """
    :type intervals: List[Interval]
        :rtype: int
    """
    if not intervals: return 0
    intervals = sorted(intervals, key = lambda x: x.start)
    minheap = []
    for i in intervals:
        if minheap and minheap[0] <= i.start:
            heapq.heapreplace(minheap,max(i.end,minheap[0))
        else:
            heapq.heappush(minheap,i.end)
    return len(minheap)
                                                        

