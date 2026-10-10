class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Initialize distance array
        # dist[i] = minimum cost to reach city i
        dist = [float('inf')] * n
        dist[src] = 0  # Starting point cost is 0

        # Step 2: Perform at most k+1 relaxations (Bellman-Ford)
        for _ in range(k + 1):  
            # Make a copy so we don't overwrite distances from the same round
            new_dist = dist.copy()
            
            # Relax all edges
            for u, v, price in flights:
                if dist[u] != float('inf') and dist[u] + price < new_dist[v]:
                    # Found a cheaper way to reach v through u
                    new_dist[v] = dist[u] + price
            
            # Update distances after this round
            dist = new_dist

        # Step 3: Return result or -1 if unreachable
        return -1 if dist[dst] == float('inf') else dist[dst]
        