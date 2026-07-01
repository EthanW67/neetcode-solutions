class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append([v,w])

        minHeap = [[0,k]]
        visit = set()
        t = 0

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in visit:
                continue
            visit.add(node1)
            t = max(t, weight1)

            for node2, weight2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap, (weight2 + weight1, node2))
        return t if len(visit) == n else -1