class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        # Directions: up, down, left, right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r, c, visited, prev_height):
            # Base cases: out of bounds, already visited, or can't flow up
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return
            
            # Mark current cell as visited
            visited.add((r, c))

            # Explore all 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # 1) Start DFS from Pacific Ocean (top row & left col)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])         # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])         # Left col
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right col

        # 2) Intersection: cells reachable by both oceans
        result = list(pacific & atlantic)
        return result
        