class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        q = deque()
        minheap = []
        time = 0
        for count in count.values():
            minheap.append(-count)
        heapq.heapify(minheap)

        while minheap or q:
            time += 1
            if minheap:
                count = heapq.heappop(minheap) + 1
                
                if count < 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(minheap, q.popleft()[0])
        return time