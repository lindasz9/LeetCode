"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        prev = 0  # Track the end time of the last meeting
        
        for i in intervals:
            if i.start >= prev:
                prev = i.end  # No overlap, update previous end time
            else:
                return False  # Overlap found, cannot attend all meetings
        
        return True  # No overlaps found, all meetings can be attended
