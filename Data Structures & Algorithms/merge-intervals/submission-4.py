class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])

        for start, end in intervals:
            endPoint = result[-1][1]
            if endPoint >= start:
                result[-1][1] = max(endPoint, end)
            else:
                result.append([start,end])

        return result 