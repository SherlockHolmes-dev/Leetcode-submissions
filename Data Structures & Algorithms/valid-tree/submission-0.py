from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                dfs(neighbor, node)
        
        dfs(0, -1)

        return len(visited) == n

        

        