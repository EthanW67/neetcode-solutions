class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        for i in range(n):
            parent.append(i)
        rank = [1] * n

        def find(n1):
            result = n1
            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return 0

            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2] 
            
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return 1
        result = n
        for n1, n2 in edges: 
            result -= union(n1, n2)
        return result