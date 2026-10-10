from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        max_frequency = max(frequency.values())
        max_freq_count = sum(1 for i in frequency.values() if i == max_frequency)

        # Result=max(length of tasks,(max frequency−1)×(n+1)+ number of tasks with max frequency)
        return max(len(tasks), (max_frequency - 1) * (n + 1) + max_freq_count)

        

        