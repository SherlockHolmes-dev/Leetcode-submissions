from collections import deque

INF = 2**31 - 1

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dq = deque()

        # 1) Enqueue all gates with distance = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r, c, 0))

        # 2) BFS from all gates simultaneously
        while dq:
            r, c, dist = dq.popleft()
            # Explore four directions
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                # If in bounds and is an empty room
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == INF):
                    # Update distance to nearest gate
                    grid[nr][nc] = dist + 1
                    # Enqueue for further propagation
                    dq.append((nr, nc, dist + 1))
        # Done—in-place modification



        