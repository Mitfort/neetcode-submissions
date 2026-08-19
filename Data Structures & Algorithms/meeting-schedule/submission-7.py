"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda i:i.start)
        
        x1,x2 = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            y1,y2 = intervals[i].start, intervals[i].end

            if y1 >= x1 and y1 < x2:
                #print(f"{x1}-{x2} | {y1}-{y2}")
                return False
            
            if y2 <= x2 and y2 > x1:
                #print(f"{x1}-{x2} | {y1}-{y2}")
                return False

            x1 = min(x1,y1)
            x2 = max(x2,y2)

        return True
