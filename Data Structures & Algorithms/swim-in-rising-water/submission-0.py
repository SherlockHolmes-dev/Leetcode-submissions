class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # Create a visited matrix to mark which cells we have already processed
        # This prevents revisiting the same cell and going into infinite loops
        visited = [[False] * n for _ in range(n)]
        
        # Min-heap (priority queue) to always process the cell
        # with the smallest "current water level" first
        # Each entry in heap: (time_to_reach_cell, row, col)
        heap = [(grid[0][0], 0, 0)]
        
        # Mark the starting cell as visited
        visited[0][0] = True
        
        # Directions array to move UP, DOWN, LEFT, RIGHT
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            # Pop the cell with the smallest current time (lowest required water level)
            time, r, c = heapq.heappop(heap)

            # If we reach the bottom-right corner, return the current time
            # because this is the earliest time we can reach this cell
            if r == n-1 and c == n-1:
                return time

            # Explore all 4-directional neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if neighbor is inside grid bounds and not visited
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # Mark neighbor as visited
                    visited[nr][nc] = True

                    # Water must be at least as high as the max elevation along the path
                    # If the neighbor is higher, we must wait until water reaches that level
                    next_time = max(time, grid[nr][nc])

                    # Push neighbor into the heap to explore later
                    # Heap ensures we always pick the path that needs the lowest water first
                    heapq.heappush(heap, (next_time, nr, nc))
            
        