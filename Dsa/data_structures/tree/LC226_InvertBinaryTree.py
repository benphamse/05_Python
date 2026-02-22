"""
LeetCode Problem #226: Invert Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Algorithm: Recursive Tree Traversal / DFS
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping the left and right children of all nodes.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            The root of the inverted binary tree
        """
        # Base case: empty tree
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


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
    
    # Helper function to convert tree to list (level-order)
    def tree_to_list(root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result
    
    # Test case 1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    print(f"Input: [4,2,7,1,3,6,9]")
    result1 = solution.invertTree(root1)
    print(f"Output: {tree_to_list(result1)}")
    print(f"Expected: [4,7,2,9,6,3,1]")
    print()
    
    # Test case 2
    root2 = build_tree([2, 1, 3])
    print(f"Input: [2,1,3]")
    result2 = solution.invertTree(root2)
    print(f"Output: {tree_to_list(result2)}")
    print(f"Expected: [2,3,1]")
    print()
    
    # Test case 3
    root3 = build_tree([])
    print(f"Input: []")
    result3 = solution.invertTree(root3)
    print(f"Output: {tree_to_list(result3)}")
    print(f"Expected: []")
