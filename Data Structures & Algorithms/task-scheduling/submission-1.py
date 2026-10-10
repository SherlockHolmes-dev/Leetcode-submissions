import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        maxheap = [-cnt for cnt in frequency.values()]
        heapq.heapify(maxheap)

        time = 0

        while maxheap:
            temp = []
            for i in range(n + 1):
                if maxheap:
                    task = heapq.heappop(maxheap)
                    if task + 1 < 0: # Since task is negative
                        temp.append(task + 1)
                time += 1

                if not maxheap and not temp:
                    break # All tasks are done
                
            for j in temp:
                heapq.heappush(maxheap, j)
            
        return time

        