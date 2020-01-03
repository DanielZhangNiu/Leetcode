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
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        minheap = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for i in range(len(intervals)):
            if minheap and minheap[0] <= intervals[i][0]: #最小的结束时间如果小于等于新元素的开始时间，说明新会议可以在接着开，不需要新的会议室，否则时间出现重叠，新开会议室
                heapq.heapreplace(minheap, intervals[i][1])
            else:
                heapq.heappush(minheap, intervals[i][1])
        return len(minheap)
