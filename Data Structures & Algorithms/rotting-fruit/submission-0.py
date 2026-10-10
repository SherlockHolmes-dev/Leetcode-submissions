from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dq = deque()
        fresh_count = 0

        # 1) Enqueue all initial rotten oranges, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes_elapsed = 0

        # 2) BFS from all rotten oranges simultaneously
        while dq:
            r, c, t = dq.popleft()
            minutes_elapsed = max(minutes_elapsed, t)

            # Spread to 4-directional neighbors
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Rot this fresh orange
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    dq.append((nr, nc, t + 1))

        # 3) If any fresh remain, it’s impossible
        return -1 if fresh_count > 0 else minutes_elapsed
        