"""
LeetCode Problem #104: Maximum Depth of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Algorithm: Recursive DFS / Tree Traversal
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (recursion stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth of a binary tree.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            The maximum depth (number of nodes from root to farthest leaf)
        """
        # Base case: empty tree has depth 0
        if not root:
            return 0
        
        # Recursively calculate depth of left and right subtrees
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # Maximum depth is 1 (current node) + max of left and right depths
        return 1 + max(leftDepth, rightDepth)


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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Input: [3,9,20,null,null,15,7]")
    print(f"Output: {solution.maxDepth(root1)}")
    print(f"Expected: 3")
    print()
    
    # Test case 2
    root2 = build_tree([1, None, 2])
    print(f"Input: [1,null,2]")
    print(f"Output: {solution.maxDepth(root2)}")
    print(f"Expected: 2")
    print()
    
    # Test case 3
    root3 = build_tree([])
    print(f"Input: []")
    print(f"Output: {solution.maxDepth(root3)}")
    print(f"Expected: 0")
