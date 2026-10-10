class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns of the grid
        rows = len(grid)
        cols = len(grid[0])

        # A set to keep track of cells that have already been visited
        visited = set()

        # Define a recursive DFS function to explore all connected land ('1') cells
        def dfs(r, c):
            # Base case: if out of bounds, return
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # If cell is water ('0') or already visited, we return
            if grid[r][c] == '0' or (r, c) in visited:
                return

            # Mark current cell as visited
            visited.add((r, c))

            # Explore all 4 adjacent directions: up, down, left, right
            dfs(r + 1, c)  # Move down
            dfs(r - 1, c)  # Move up
            dfs(r, c + 1)  # Move right
            dfs(r, c - 1)  # Move left

        # Initialize island count to 0
        count = 0

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land and hasn't been visited
                if grid[r][c] == '1' and (r, c) not in visited:
                    # This is a new island
                    count += 1
                    # Perform DFS to visit all land connected to this cell
                    dfs(r, c)

        # After traversing the entire grid, return the total island count
        return count
        