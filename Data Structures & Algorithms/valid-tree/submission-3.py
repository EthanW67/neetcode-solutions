class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adjMap = defaultdict(list)

        for node, preq in edges:
            adjMap[node].append(preq)
            adjMap[preq].append(node)

        visit = set()
        def dfs(nodes, prev):
            if nodes in visit:
                return False
            visit.add(nodes)
            for nei in adjMap[nodes]:
                if nei == prev:
                    continue
                if not dfs(nei, nodes):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)