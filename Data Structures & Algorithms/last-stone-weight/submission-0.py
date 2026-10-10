import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max-heap by pushing negatives
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # Continue smashing the two heaviest stones
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap) # Heaviest
            second = -heapq.heappop(max_heap) # Second heaviest

            # If they are not equal, push the difference back
            if first != second:
                heapq.heappush(max_heap, -(first-second))

        # If heap is not empty, return the remaining stone (invert sign)           
        return -max_heap[0] if max_heap else 0
        