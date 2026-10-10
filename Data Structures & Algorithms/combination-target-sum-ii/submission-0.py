class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily

        def backtrack(start, path, currentSum):
            if currentSum == target:
                res.append(path[:])  # Found a valid combination
                return
            if currentSum > target:
                return  # Exceeded the target, no need to continue

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # Include candidates[i] in the current combination
                path.append(candidates[i])

                # Move to the next index (each number can be used at most once)
                backtrack(i + 1, path, currentSum + candidates[i])

                # Backtrack: remove the last element
                path.pop()

        backtrack(0, [], 0)
        return res
        