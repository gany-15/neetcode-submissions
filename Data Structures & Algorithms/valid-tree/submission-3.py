class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        st = [(None, 0)]
        while st:
            parent, root = st.pop()
            visited.add(root)
            for node in adj[root]:
                if node != parent and node not in visited:
                    st.append((root, node))
                elif node != parent and node in visited:
                    return False
        
        return True
