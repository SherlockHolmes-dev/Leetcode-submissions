import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build graph with min-heaps for lexicographic order
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        res = []  # This will store our itinerary in reverse

        def dfs(airport):
            # Explore all outgoing flights from current airport
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])  # Smallest lexicographic airport
                dfs(next_airport)  # Recursively visit next
            res.append(airport)  # Post-order add

        # Step 2: Start DFS from JFK
        dfs("JFK")

        # Step 3: Reverse the result for correct itinerary order
        return res[::-1]
        