from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: Tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Step 2: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 3: DFS to check connectivity
        visited = set()

        def dfs(node: int, parent: int):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph[node]:
                # Skip the node we came from
                if neighbor == parent:
                    continue
                dfs(neighbor, node)

        dfs(0, -1)  # Start from node 0 with no parent

        # Step 4: Check if all nodes are visited (connected)
        return len(visited) == n

        

        