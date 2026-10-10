class TrieNode:
    def __init__(self):
        self.children = {}   # Maps character to next TrieNode
        self.isWord = False  # True if a word ends at this node

class PrefixTree:

    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        # Traverse each character in the word
        for ch in word:
            # If the character is not yet in children, create a new node
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # Move to the child node
            node = node.children[ch]
        # After inserting all characters, mark the end of a valid word
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        # Traverse the Trie following the characters in the word
        for ch in word:
            if ch not in node.children:
                return False  # If any character is missing, word doesn't exist
            node = node.children[ch]
        # At the end, return True only if this node marks the end of a word
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        # Traverse the Trie following the characters in the prefix
        for ch in prefix:
            if ch not in node.children:
                return False  # If any character is missing, prefix doesn't exist
            node = node.children[ch]
        # All characters in prefix matched successfully
        return True
        
        