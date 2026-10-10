class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Set to track visited land cells
        visited = set()

        def dfs(r, c):
            # If out of bounds, water, or already visited, return 0
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == 0 or (r, c) in visited
            ):
                return 0
            
            # Mark this cell as visited
            visited.add((r, c))

            # Start with area 1 for the current land cell
            area = 1

            # Recursively visit all 4 directions and add their area
            area += dfs(r + 1, c)  # Down
            area += dfs(r - 1, c)  # Up
            area += dfs(r, c + 1)  # Right
            area += dfs(r, c - 1)  # Left

            return area

        max_area = 0

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not yet visited
                if grid[r][c] == 1 and (r, c) not in visited:
                    # Start DFS and compute area of this island
                    current_area = dfs(r, c)
                    # Update maximum area seen so far
                    max_area = max(max_area, current_area)

        return max_area
        