class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hour = math.ceil(pile / mid)
                hours += hour
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
        