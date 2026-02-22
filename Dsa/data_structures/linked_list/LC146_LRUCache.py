"""
LeetCode Problem #146: LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Algorithm: Hash Map + Doubly Linked List (or OrderedDict)
Time Complexity: O(1) for get and put
Space Complexity: O(capacity)
"""

from typing import Optional


# Solution 1: Using OrderedDict (Python-specific, cleaner)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache.pop(key)
        self.cache[key] = val
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[next(iter(self.cache))]
        
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Solution 2: Using Doubly Linked List + Hash Map (Interview standard)
class Node:
    """Doubly linked list node for LRU cache."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache2:
    def __init__(self, capacity: int):
        """
        Initialize LRU Cache with doubly linked list.
        
        Args:
            capacity: Maximum number of items in cache
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node: Node) -> None:
        """Move existing node to head (mark as recently used)."""
        self._remove(node)
        self._add_to_head(node)
    
    def _remove_tail(self) -> Node:
        """Remove and return least recently used node (before tail)."""
        lru_node = self.tail.prev
        self._remove(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        """
        Get value from cache and mark as recently used.
        
        Args:
            key: Key to lookup
        
        Returns:
            Value if key exists, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair in cache. Evict LRU if needed.
        
        Args:
            key: Key to store
            value: Value to store
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove least recently used
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]


# Test cases
if __name__ == "__main__":
    print("=== Testing LRUCache (OrderedDict) ===")
    
    # Test case 1: Basic operations
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"get(1): {cache.get(1)}")  # Expected: 1
    cache.put(3, 3)  # Evicts key 2
    print(f"get(2): {cache.get(2)}")  # Expected: -1 (evicted)
    cache.put(4, 4)  # Evicts key 1
    print(f"get(1): {cache.get(1)}")  # Expected: -1 (evicted)
    print(f"get(3): {cache.get(3)}")  # Expected: 3
    print(f"get(4): {cache.get(4)}")  # Expected: 4
    print()
    
    # Test case 2: Update existing key
    cache2 = LRUCache(2)
    cache2.put(2, 1)
    cache2.put(2, 2)  # Update
    print(f"get(2): {cache2.get(2)}")  # Expected: 2
    cache2.put(1, 1)
    cache2.put(4, 1)  # Evicts key 2
    print(f"get(2): {cache2.get(2)}")  # Expected: -1
    print()
    
    print("=== Testing LRUCache2 (Doubly Linked List) ===")
    
    # Test case 3: Same as test case 1 with manual implementation
    cache3 = LRUCache2(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    print(f"get(1): {cache3.get(1)}")  # Expected: 1
    cache3.put(3, 3)  # Evicts key 2
    print(f"get(2): {cache3.get(2)}")  # Expected: -1 (evicted)
    cache3.put(4, 4)  # Evicts key 1
    print(f"get(1): {cache3.get(1)}")  # Expected: -1 (evicted)
    print(f"get(3): {cache3.get(3)}")  # Expected: 3
    print(f"get(4): {cache3.get(4)}")  # Expected: 4
