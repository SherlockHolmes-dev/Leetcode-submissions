from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        
        return components

        

        