
"""
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
    
    You may assume that the intervals were initially sorted according to their start times.
    
    Example 1:
    
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    Example 2:
    
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) == 0 and newInterval:
        return [newInterval]
    
    intervals.append(newInterval)
    intervals = sorted(intervals, key = lambda x: x.start)
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1].end >= intervals[i].start:
            res[-1].end = max(res[-1].end, intervals[i].end)
        else:
            res.append(intervals[i])
    return res
