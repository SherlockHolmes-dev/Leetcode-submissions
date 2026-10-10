class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store full word at the end node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = TrieNode()

        # Step 1: Build Trie from word list
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # Mark the end of the word

        rows, cols = len(board), len(board[0])

        # Step 2: DFS from each cell
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a word
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark current cell as visited
            board[r][c] = '#'

            # Explore 4 directions
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # Restore the original character (backtrack)
            board[r][c] = char

            # Optional Trie pruning for performance
            if not next_node.children:
                node.children.pop(char)

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return res