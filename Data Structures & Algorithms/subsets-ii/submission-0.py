class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        res = []

        def backtrack(start, path):
            res.append(path[:])  # Add current subset

            for i in range(start, len(nums)):
                # Skip duplicates in the same recursive level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose nums[i]
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return res
        