from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = {}

        for word in words:
            for char in word:
                in_degree[char] = 0
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
        
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == len(in_degree):
            return "".join(order)
        else:
            return ""

        