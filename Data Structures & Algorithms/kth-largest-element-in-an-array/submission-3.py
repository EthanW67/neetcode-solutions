class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(len(nums)):
            minheap.append(-nums[i])
        heapq.heapify(minheap)
        while k > 0:
            k -= 1

            result = heapq.heappop(minheap)
        return -result