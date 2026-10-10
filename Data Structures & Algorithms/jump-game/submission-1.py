class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Backward Greedy Solution
        target = len(nums) - 1  # Start with last index as the target

        # Move backwards through the array
        for i in range(len(nums) - 2, -1, -1):
            # If we can jump from i to target or beyond
            if i + nums[i] >= target:
                target = i  # Move the target backward
        
        # If we could move target to the first index
        return target == 0
        