from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Step 1: Precompute pattern mapping
        pattern_map = defaultdict(list)
        wordLen = len(beginWord)
        
        for word in wordSet:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
        
        # Step 2: BFS queue -> (word, level)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()
            
            # Step 3: Generate all possible generic patterns for current word
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i+1:]
                
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear to avoid redundant processing
                pattern_map[pattern] = []
        
        return 0  # No transformation found

        