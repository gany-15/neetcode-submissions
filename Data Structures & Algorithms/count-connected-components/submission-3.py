class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(v):
            while v != par[v]:
                v = par[par[v]]
            return v

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return 1

        num = n
        for v1, v2 in edges:
            num -= union(v1, v2)
        return num
