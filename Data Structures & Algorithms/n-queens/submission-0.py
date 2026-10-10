class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        diag = set()      # row - col
        anti_diag = set() # row + col

        def backtrack(row):
            # If we've placed queens in all rows
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                # If this column or diagonal is under attack, skip
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue

                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack and remove queen
                board[row][col] = '.'
                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return res
        