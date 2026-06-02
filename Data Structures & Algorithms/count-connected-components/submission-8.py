class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(node):
            while parent[node] != node:
                node = parent[parent[node]]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
        
        parent = [i for i in range(n)]
        rank = [1] * n

        for i, j in edges:
            union(i, j)
        
        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1
        return count
