class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            # Base case: complete permutation
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue  # Skip used elements

                # Choose nums[i]
                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # Backtrack
                path.pop()
                used[i] = False

        backtrack([])
        return res
        