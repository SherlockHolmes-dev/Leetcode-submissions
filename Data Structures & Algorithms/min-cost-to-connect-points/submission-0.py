import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n   # Track points already in MST
        min_heap = [(0, 0)]     # (cost, point_index), start with point 0
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, point = heapq.heappop(min_heap)
            
            # Skip if this point is already in MST
            if visited[point]:
                continue
            
            # Add this point to MST
            visited[point] = True
            total_cost += cost
            edges_used += 1

            # Push all edges from this new point to non-MST points
            for next_point in range(n):
                if not visited[next_point]:
                    x1, y1 = points[point]
                    x2, y2 = points[next_point]
                    new_cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (new_cost, next_point))

        return total_cost
        