import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1
        
        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first
        