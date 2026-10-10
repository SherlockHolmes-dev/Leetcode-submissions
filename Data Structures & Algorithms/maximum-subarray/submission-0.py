class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]       # Global max sum found so far
        current_sum = 0         # Current subarray sum

        for num in nums:
            current_sum += num  # Extend the current subarray

            # Update global max if current subarray is better
            max_sum = max(max_sum, current_sum)

            # If current sum is negative, discard it (start new subarray)
            if current_sum < 0:
                current_sum = 0

        return max_sum
        