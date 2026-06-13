class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []
        for stone in stones:
            minheap.append(-stone)
        heapq.heapify(minheap)        

        while len(minheap) > 1:

            stone1 = heapq.heappop(minheap)
            stone2 = heapq.heappop(minheap)

            if -stone1 > -stone2:
                heapq.heappush(minheap, -(abs(stone1) - abs(stone2)))
            
        minheap.append(0)
        return -minheap[0]







        # heapq.heapify_max(stones)
        # print(stones)

        # while len(stones) > 1:
        #     stone1 = heapq.heappop(stones)
        #     stone2 = heapq.heappop(stones)

        #     if stone1 > stone2:
        #         heapq.heappush(stones, stone1-stone2)
        # print(stones)
        # return stones[0]
        