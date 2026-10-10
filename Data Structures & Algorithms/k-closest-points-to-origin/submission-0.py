import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = -(x*x + y*y)
            heapq.heappush(heap, (distance, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [points for i, points in heap]
        