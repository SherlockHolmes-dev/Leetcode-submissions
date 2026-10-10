import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap of size k
        minHeap = []
        
        for num in nums:
            heapq.heappush(minHeap, num)
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # The top of the heap is the k-th largest
        return minHeap[0]
        