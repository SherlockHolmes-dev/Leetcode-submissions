from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        
        # Directions for up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Initialize queue with all treasure cells (0)
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # BFS from all treasure cells
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and if cell is land and can be updated with shorter distance
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    # If current distance + 1 is less than neighbor's distance, update it
                    if grid[nr][nc] > grid[r][c] + 1:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))