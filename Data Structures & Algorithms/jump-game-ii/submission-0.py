class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0          # Count of jumps made
        current_end = 0    # Current jump boundary
        farthest = 0       # Farthest index reachable so far

        # We iterate to n-2 because reaching the last index ends the process
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])  # Update farthest reach
            
            # If we have reached the end of the current jump range
            if i == current_end:
                jumps += 1             # Take a jump
                current_end = farthest # Update the boundary of the next jump

        return jumps
        