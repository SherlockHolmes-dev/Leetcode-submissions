class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()  # Sorting helps in pruning

        def backtrack(start, path, currentSum):
            if currentSum == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                # Prune if the candidate is too large
                if currentSum + nums[i] > target:
                    break  # Since array is sorted, no need to check further

                path.append(nums[i])
                backtrack(i, path, currentSum + nums[i])  # Not i + 1 because we can reuse
                path.pop()

        backtrack(0, [], 0)
        return res
        