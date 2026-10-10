class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Left = LRU, Right = MRU
        self.left = Node(0, 0)  # dummy LRU
        self.right = Node(0, 0) # dummy MRU
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert at MRU (before right)
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node   

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move node to front
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
