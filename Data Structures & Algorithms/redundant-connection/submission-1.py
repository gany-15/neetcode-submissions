class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            while parent[node] != node:
                node = parent[parent[node]]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += p1
            else:
                parent[p2] = p1
                rank[p1] += p2
        
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        for i, j in edges:
            if union(i, j):
                return [i, j]
        return []
