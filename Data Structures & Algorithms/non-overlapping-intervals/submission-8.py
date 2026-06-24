class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        result = 0
        intervals.sort()
        stack.append(intervals[0])
        for start, end in intervals[1:]:
            endPoint = stack[-1][1]
            if endPoint > start:
                result += 1
                if end < endPoint:
                    stack[-1] = [start,end]
                continue
            stack.append([start, end])
        return result
# interval=[[0,2],[1,3],[2,4],[3,5],[4,6]]
# interval.sort()
# print(interval)



# Input: intervals = [[1,2],[1,4],[2,4]]















        # result = 0
        # intervals.sort()
        # prevEnd = intervals[0][1]
        # for start, end in intervals[1:]:
        #     if prevEnd > start:
        #         result += 1
        #         prevEnd = min(prevEnd, end)
        #     else:
        #         prevEnd = end
        # return result




    # Input: intervals = [[1,2],[1,4],[2,4]]
