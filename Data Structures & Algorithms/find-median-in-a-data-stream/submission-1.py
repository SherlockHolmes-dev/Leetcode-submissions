import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (inverted values for lower half)
        self.left = []
        # Min-heap (for upper half)
        self.right = []
        

    def addNum(self, num: int) -> None:
        # Push to max-heap (invert to simulate max-heap)
        heapq.heappush(self.left, -num)
        
        # Balance: Move max from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        
        # Maintain size property
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        # If odd, max-heap has one extra element
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, average of two middle values
        return (-self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()