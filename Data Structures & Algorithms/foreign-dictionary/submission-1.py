from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph structures
        graph = defaultdict(set)  # adjacency list: char -> set of next chars
        indegree = {}             # indegree count for each char
        
        # Add all unique characters to indegree dict (start with 0)
        for word in words:
            for char in word:
                indegree[char] = 0
        
        # Step 2: Build edges between characters
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            
            # Case: prefix conflict -> invalid
            # Example: ["abc", "ab"] is invalid because "abc" should come after "ab"
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            # Compare characters to find first difference
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    # If c2 not already a neighbor of c1, add edge and update indegree
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break  # Only first difference matters
                    # If no difference found, just continue
        
        # Step 3: Topological sort using Kahn's algorithm
        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            
            # For all neighbors, reduce indegree
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if topological sort included all characters
        if len(order) == len(indegree):
            return "".join(order)
        else:
            # Cycle detected -> invalid ordering
            return ""

        