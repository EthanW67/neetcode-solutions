class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = collections.defaultdict(list)
        for i, equat in enumerate(equations):
            a, b = equat
            adjMap[a].append([b, values[i]])
            adjMap[b].append([a, 1/ values[i]])
        print(adjMap)

        def bfs(src, target):
            if src not in adjMap or target not in adjMap: 
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight

                for nei, weight2 in adjMap[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, weight2 * weight])

            return -1
        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result
