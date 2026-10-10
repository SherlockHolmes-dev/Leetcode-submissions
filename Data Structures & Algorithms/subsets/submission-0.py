class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # Append the current subset (copy to avoid reference issues)
            res.append(path[:])

            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Recurse with the next index
                backtrack(i + 1, path)
                # Backtrack: remove the last element before moving to the next
                path.pop()

        backtrack(0, [])
        return res
        