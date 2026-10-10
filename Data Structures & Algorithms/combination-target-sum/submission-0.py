class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, currentSum):
            # Base case: found a valid combination
            if currentSum == target:
                res.append(path[:])
                return

            # If current sum exceeds target, stop exploring this path
            if currentSum > target:
                return

            # Try each candidate starting from 'start' to allow unlimited usage of the same number
            for i in range(start, len(nums)):
                # Include nums[i] in the combination
                path.append(nums[i])
                # Recurse with the same index i (allowing repeat usage)
                backtrack(i, path, currentSum + nums[i])
                # Backtrack: remove the last added number
                path.pop()

        # Start the backtracking with empty path and sum 0
        backtrack(0, [], 0)
        return res
        