class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        # Recursive DFS function
        def dfs(i):
            # Base case: reached end of string
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                # Check if substring s[i..j] is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])  # Choose
                    dfs(j + 1)                 # Explore
                    part.pop()                # Un-choose (backtrack)

        dfs(0)
        return res

    # Helper to check if s[l..r] is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        