"""
LeetCode Problem #110: Balanced Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
of every node never differs by more than one.

Algorithm: Recursive DFS with Height Calculation
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            True if the tree is balanced, False otherwise
        """
        return self.height(root) != -1
    
    def height(self, node: Optional[TreeNode]) -> int:
        """
        Calculate height of the tree and check if balanced.
        
        Args:
            node: Current node being processed
            
        Returns:
            Height of the subtree if balanced, -1 if unbalanced
        """
        if not node:
            return 0
        
        # Get height of left and right subtrees
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        
        # If left or right subtree is unbalanced, propagate -1
        if leftHeight == -1 or rightHeight == -1:
            return -1
        
        # If current node is unbalanced, return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        # Return height of current node
        return 1 + max(leftHeight, rightHeight)


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
    
    # Test case 1: Balanced tree
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Input: [3,9,20,null,null,15,7]")
    print(f"Output: {solution.isBalanced(root1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2: Unbalanced tree
    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(f"Input: [1,2,2,3,3,null,null,4,4]")
    print(f"Output: {solution.isBalanced(root2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3: Empty tree
    root3 = build_tree([])
    print(f"Input: []")
    print(f"Output: {solution.isBalanced(root3)}")
    print(f"Expected: True")
