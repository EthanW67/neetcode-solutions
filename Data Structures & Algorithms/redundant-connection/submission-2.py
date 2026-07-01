class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges) + 1)
        parent = []
        for i in range(len(edges) + 1):
            parent.append(i)



        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False
            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return True

        for edge1, edge2 in edges:
            if not union(edge1, edge2):

                return [edge1,edge2]

