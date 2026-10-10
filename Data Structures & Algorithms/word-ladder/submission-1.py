from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to set for O(1) lookups
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0  # Cannot reach endWord if it's not in the dictionary

        # Initialize frontiers for bidirectional BFS
        begin_set = {beginWord}  # Start BFS from the beginWord
        end_set = {endWord}      # Start BFS from the endWord
        visited = set()          # Keep track of visited words to avoid cycles
        level = 1                # Start at level 1 (counting the beginWord itself)
        L = len(beginWord)       # All words are of the same length

        # BFS loop until one of the frontiers becomes empty
        while begin_set and end_set:
            # Always expand the smaller frontier to reduce search space
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()  # Will hold the next level's frontier

            # Explore all words in the current frontier
            for word in begin_set:
                # Try changing every position in the word
                for i in range(L):
                    for c in ascii_lowercase:
                        # Create a new word by replacing one character
                        new_word = word[:i] + c + word[i+1:]

                        # If the new word is in the opposite frontier, path is found
                        if new_word in end_set:
                            return level + 1

                        # If the new word is valid and not visited yet
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)   # Mark as visited
                            next_set.add(new_word) # Add to next frontier

            # Move to the next level
            begin_set = next_set
            level += 1

        # If BFS ends without finding a path
        return 0

        