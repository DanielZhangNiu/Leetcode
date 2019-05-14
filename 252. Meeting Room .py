"""
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
    
    Example 1:
    
    Input: [[0,30],[5,10],[15,20]]
    Output: false
    Example 2:
    
    Input: [[7,10],[2,4]]
    Output: true
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def canAttendMeetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    if not intervals:
        return True
    intervals.sort(key = lambda x:x[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True
