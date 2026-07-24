"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starting, ending = [], []
        for i in intervals:
            starting.append(i.start)
            ending.append(i.end)
        starting.sort()
        ending.sort()
        result, count = 0, 0
        s, e  = 0, 0
        while s < len(intervals):
            if starting[s] < ending[e]:
                s+=1
                count += 1
            else:
                e+= 1
                count -= 1
            result = max(result, count)

        return result