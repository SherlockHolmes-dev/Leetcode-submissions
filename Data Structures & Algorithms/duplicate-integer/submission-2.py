class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        n = len(nums)

        for i in range(0, n):
            if nums[i] in dup:
                return True
            dup.add(nums[i])
        
        return False
        