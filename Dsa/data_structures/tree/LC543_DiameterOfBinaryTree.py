"""
LeetCode Problem #543: Diameter of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Algorithm: Recursive DFS with Global Variable
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Returns the diameter of a binary tree (longest path between any two nodes).
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            The diameter (number of edges in the longest path)
        """
        self.diameter = 0
        self.height(root)
        return self.diameter
    
    def height(self, node: Optional[TreeNode]) -> int:
        """
        Calculate height of the tree and update diameter.
        
        Args:
            node: Current node being processed
            
        Returns:
            Height of the subtree rooted at node
        """
        if not node:
            return 0
        
        # Get height of left and right subtrees
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        
        # Update diameter: path through current node
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        
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
    
    # Test case 1
    root1 = build_tree([1, 2, 3, 4, 5])
    print(f"Input: [1,2,3,4,5]")
    print(f"Output: {solution.diameterOfBinaryTree(root1)}")
    print(f"Expected: 3 (Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)")
    print()
    
    # Test case 2
    root2 = build_tree([1, 2])
    print(f"Input: [1,2]")
    print(f"Output: {solution.diameterOfBinaryTree(root2)}")
    print(f"Expected: 1")
    print()
    
    # Test case 3
    root3 = build_tree([1, 2, 3, 4, 5, None, None, 6, 7])
    print(f"Input: [1,2,3,4,5,null,null,6,7]")
    print(f"Output: {solution.diameterOfBinaryTree(root3)}")
    print(f"Expected: 5 (Path: 6 -> 4 -> 2 -> 5 or 7 -> 4 -> 2 -> 5)")
