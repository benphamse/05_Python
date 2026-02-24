"""
LeetCode Problem #100: Same Tree
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Algorithm: Recursive DFS / Tree Traversal
Time Complexity: O(min(n, m)) where n and m are the number of nodes in trees p and q
Space Complexity: O(min(h1, h2)) where h1 and h2 are the heights of trees p and q (recursion stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical.
        
        Two trees are considered the same if they are structurally identical
        and the nodes have the same values.
        
        Args:
            p: Root of the first binary tree
            q: Root of the second binary tree
        
        Returns:
            True if trees are identical, False otherwise
        """
        # Base case: both nodes are None
        if not p and not q:
            return True
        
        # One is None, the other is not
        if not p or not q:
            return False
        
        # Check current nodes and recursively check subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Helper function to build tree from list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(nodes):
                    node.left = nodes[left_idx]
                if right_idx < len(nodes):
                    node.right = nodes[right_idx]
        return nodes[0]
    
    # Test case 1
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(f"Input: p = [1,2,3], q = [1,2,3]")
    print(f"Output: {solution.isSameTree(p1, q1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print(f"Input: p = [1,2], q = [1,null,2]")
    print(f"Output: {solution.isSameTree(p2, q2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(f"Input: p = [1,2,1], q = [1,1,2]")
    print(f"Output: {solution.isSameTree(p3, q3)}")
    print(f"Expected: False")
