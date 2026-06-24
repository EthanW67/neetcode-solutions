"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
            

        interval = []
        for int in intervals:
            interval.append([int.start,int.end])
        interval.sort()
        stack =[]
        stack.append(interval[0])

        for start, end in interval[1:]:
            endPoint = stack[-1][1]
            if endPoint > start:
                return False
            stack.append([start,end])
        return True


            