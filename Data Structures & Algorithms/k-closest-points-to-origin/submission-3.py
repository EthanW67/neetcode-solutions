from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for value in points:
            distance = sqrt((value[0] - 0)**2 + (value[1] - 0)**2)
            heapq.heappush(minheap,[distance, value])
        result = []
        while k > 0:
            k -= 1
            val = heapq.heappop(minheap)
            result.append(val[-1])
        return result