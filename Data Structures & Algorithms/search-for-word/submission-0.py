class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Helper DFS function
        def dfs(r, c, index):
            # All characters matched
            if index == len(word):
                return True

            # Out of bounds or character mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False

            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all four directions
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))

            # Restore the original character (backtrack)
            board[r][c] = temp

            return found

        # Try to start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
        