import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k

        # Initialize heap with nums
        for num in nums:
            self.add(num) # Reuse add function to handle logic
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val) # Push new value

        # If heap exceeds size k, remove smallest element
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        # The kth largest element is the smallest in the heap       
        return self.minheap[0]
        
