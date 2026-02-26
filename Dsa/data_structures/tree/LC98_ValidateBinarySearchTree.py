"""
LeetCode Problem #98: Validate Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Algorithm: Recursive DFS with Range Validation
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate if a binary tree is a valid Binary Search Tree.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self, node: Optional[TreeNode], minVal: float, maxVal: float) -> bool:
        """
        Helper method to validate BST with range constraints.
        
        Args:
            node: Current node being validated
            minVal: Minimum allowed value for this node
            maxVal: Maximum allowed value for this node
            
        Returns:
            True if subtree is valid BST, False otherwise
        """
        # Base case: empty tree is valid BST
        if not node:
            return True
        
        # Current node's value must be within the valid range
        if not (minVal < node.val < maxVal):
            return False
        
        # Recursively validate left and right subtrees
        # Left subtree: all values must be less than current node
        # Right subtree: all values must be greater than current node
        return (self.validate(node.left, minVal, node.val) and 
                self.validate(node.right, node.val, maxVal))


# Alternative Solution 1: Iterative with Stack
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative approach using stack with (node, min, max) tuples.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, minVal, maxVal = stack.pop()
            
            if not (minVal < node.val < maxVal):
                return False
            
            if node.right:
                stack.append((node.right, node.val, maxVal))
            if node.left:
                stack.append((node.left, minVal, node.val))
        
        return True


# Alternative Solution 2: In-order Traversal
class Solution3:
    def __init__(self):
        self.prev = float('-inf')
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        In-order traversal of BST should be strictly increasing.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        return self.inorder(root)
    
    def inorder(self, node: Optional[TreeNode]) -> bool:
        """
        Perform in-order traversal and check if values are strictly increasing.
        
        Args:
            node: Current node being processed
            
        Returns:
            True if subtree maintains strictly increasing order, False otherwise
        """
        if not node:
            return True
        
        # Check left subtree
        if not self.inorder(node.left):
            return False
        
        # Check current node
        if node.val <= self.prev:
            return False
        self.prev = node.val
        
        # Check right subtree
        return self.inorder(node.right)


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
    
    # Test case 1: Valid BST
    root1 = build_tree([2, 1, 3])
    print(f"Input: [2,1,3]")
    print(f"Output: {solution.isValidBST(root1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2: Invalid BST (left subtree has value greater than root)
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print(f"Input: [5,1,4,null,null,3,6]")
    print(f"Output: {solution.isValidBST(root2)}")
    print(f"Expected: False (node 4 is in right subtree but < 5)")
    print()
    
    # Test case 3: Single node (valid BST)
    root3 = build_tree([1])
    print(f"Input: [1]")
    print(f"Output: {solution.isValidBST(root3)}")
    print(f"Expected: True")
