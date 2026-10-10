class TrieNode:
    def __init__(self):
        self.children = {}   # Maps character -> TrieNode
        self.isWord = False  # True if this node ends a word

class WordDictionary:

    def __init__(self):
        # Root of the Trie
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        # Insert each character into the Trie
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # Mark the end of a complete word
        node.isWord = True
        

    def search(self, word: str) -> bool:
        # Helper DFS function to support '.'
        def dfs(j, node):
            # Traverse the word from index j
            for i in range(j, len(word)):
                ch = word[i]

                # If the character is '.', we try all children
                if ch == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False  # No child matched
                else:
                    # If regular character doesn't exist, return False
                    if ch not in node.children:
                        return False
                    node = node.children[ch]  # Move to child node

            # After last character, check if we're at a valid word
            return node.isWord

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)