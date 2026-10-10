import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize Dijkstra
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0  # Distance to source is 0
        min_heap = [(0, k)]  # (distance, node)

        # Step 3: Dijkstra's algorithm using min-heap
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            # Skip if we already found a shorter path
            if curr_dist > dist[node]:
                continue

            # Relax edges
            for nei, w in graph[node]:
                new_dist = curr_dist + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(min_heap, (new_dist, nei))

        # Step 4: Compute result
        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1
        