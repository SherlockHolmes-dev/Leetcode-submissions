class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitToChar = {
            '2': "abc", '3': "def",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        # Recursive DFS function
        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))  # Base case: full combination
                return

            for ch in digitToChar[digits[i]]:
                path.append(ch)       # Choose a letter
                backtrack(i + 1, path)  # Explore further
                path.pop()            # Backtrack

        backtrack(0, [])
        return res
        