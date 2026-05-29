class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            parent = par[node]

            while parent != par[parent]:
                par[parent] = par[par[parent]]
                parent = par[parent]
            
            return parent
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 != parent2:
                if rank[parent1] >= rank[parent2]:
                    par[parent2] = parent1
                    rank[parent1] += rank[parent2]
                else:
                    par[parent1] = parent2
                    rank[parent2] += rank[parent1]
                return 1
            return 0
        
        for a, b in edges:
            components -= union(a, b)
        
        return components
