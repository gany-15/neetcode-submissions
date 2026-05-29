class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps = n
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            par = parent[node]

            while par != parent[par]:
                parent[node] = parent[parent[node]]
                par = parent[node]
            
            return par
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for x, y in edges:
            comps -= union(x, y)
        
        return comps
