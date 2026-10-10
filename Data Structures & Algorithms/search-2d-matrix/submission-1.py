class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            ROW = (top + bot) //2
            if target > matrix[ROW][-1]:
                top = ROW + 1
            elif target < matrix[ROW][0]:
                bot = ROW - 1
            else:
                break
            
        if not (top <= bot):
            return False
        
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[ROW][m]:
                l = m + 1
            elif target < matrix[ROW][m]:
                r = m - 1
            else:
                return True
        return False
        