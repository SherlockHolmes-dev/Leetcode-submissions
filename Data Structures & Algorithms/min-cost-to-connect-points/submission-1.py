class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Start with point 0
        total_cost = 0

        for _ in range(n):
            # Step 1: Pick unvisited point with smallest connection cost
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_cost[i] < min_cost[u]):
                    u = i

            # Step 2: Add point u to MST
            visited[u] = True
            total_cost += min_cost[u]

            # Step 3: Update cost to connect remaining points
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_cost[v]:
                        min_cost[v] = dist

        return total_cost

        
        