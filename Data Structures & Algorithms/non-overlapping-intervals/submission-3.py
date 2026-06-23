class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd > start:
                result += 1
            
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return result




    # Input: intervals = [[1,2],[1,4],[2,4]]
