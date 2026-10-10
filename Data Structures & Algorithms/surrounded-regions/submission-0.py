class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])

        # Directions for DFS: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c):
            # Base case: if out of bounds or not 'O', skip
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Temporarily mark this 'O' as 'S' (safe)
            board[r][c] = 'S'

            # Explore all 4 directions from current cell
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step 1: Run DFS for 'O's on the border to mark safe 'O's
        for r in range(rows):
            # First and last column
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for c in range(cols):
            # First and last row
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Step 2: Flip all remaining 'O's to 'X' (they're surrounded)
        #         Convert all 'S' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Surrounded region
                elif board[r][c] == 'S':
                    board[r][c] = 'O'  # Restore safe region
        