"""
LeetCode Problem #572: Subtree of Another Tree
Difficulty: Easy
Link: https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree 
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this node's 
descendants. The tree could also be considered as a subtree of itself.

Algorithm: Recursive DFS / Tree Traversal
Time Complexity: O(n * m) where n is the number of nodes in root and m is the number of nodes in subRoot
Space Complexity: O(h) where h is the height of the root tree (recursion stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if subRoot is a subtree of root.
        
        Args:
            root: Root of the main binary tree
            subRoot: Root of the potential subtree
        
        Returns:
            True if subRoot is a subtree of root, False otherwise
        """
        # Base case: if subRoot is None, it's always a subtree
        if not subRoot:
            return True
        
        # If root is None but subRoot is not, subRoot cannot be a subtree
        if not root:
            return False
        
        # Check if trees rooted at current node are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Helper method to check if two trees are identical.
        
        Args:
            p: Root of first tree
            q: Root of second tree
        
        Returns:
            True if trees are identical, False otherwise
        """
        # Both nodes are None
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
    root1 = build_tree([3, 4, 5, 1, 2])
    subRoot1 = build_tree([4, 1, 2])
    print(f"Input: root = [3,4,5,1,2], subRoot = [4,1,2]")
    print(f"Output: {solution.isSubtree(root1, subRoot1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot2 = build_tree([4, 1, 2])
    print(f"Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]")
    print(f"Output: {solution.isSubtree(root2, subRoot2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3
    root3 = build_tree([1, 1])
    subRoot3 = build_tree([1])
    print(f"Input: root = [1,1], subRoot = [1]")
    print(f"Output: {solution.isSubtree(root3, subRoot3)}")
    print(f"Expected: True")
