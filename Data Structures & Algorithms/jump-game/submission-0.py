class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Forward Greedy Solution
        farthest = 0  # Farthest index we can reach

        for i in range(len(nums)):
            # If current index is not reachable
            if i > farthest:
                return False
            
            # Update farthest reachable index
            farthest = max(farthest, i + nums[i])
            
            # Early stop if we can already reach the end
            if farthest >= len(nums) - 1:
                return True

        return True  # If loop completes, we can reach the end
        