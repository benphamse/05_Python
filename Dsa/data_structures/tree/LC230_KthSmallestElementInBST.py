"""
LeetCode Problem #230: Kth Smallest Element in a BST
Difficulty: Medium
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.

Algorithm: In-order Traversal (Iterative & Recursive)
Time Complexity: O(H + k) where H is the height of the tree
Space Complexity: O(H) for the stack/recursion
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest element in a BST using iterative in-order traversal.
        
        In-order traversal of a BST visits nodes in ascending order.
        We use a stack to simulate the traversal and count nodes until we reach k.
        
        Args:
            root: The root node of the BST
            k: The kth position (1-indexed) to find
        
        Returns:
            The kth smallest value in the BST
        """
        stack = []
        currentNode = root
        count = 0
        
        while currentNode or stack:
            # Go to the leftmost node
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            
            # Process the current node
            currentNode = stack.pop()
            count += 1
            
            # If this is the kth node, return its value
            if count == k:
                return currentNode.val
            
            # Move to the right subtree
            currentNode = currentNode.right
        
        return -1  # Should never reach here if k is valid


class SolutionRecursive:
    """Alternative solution using recursive in-order traversal"""
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest element in a BST using recursive in-order traversal.
        
        Args:
            root: The root node of the BST
            k: The kth position (1-indexed) to find
        
        Returns:
            The kth smallest value in the BST
        """
        self.k = k
        self.result = None
        self.inorderTraversal(root)
        return self.result
    
    def inorderTraversal(self, node: Optional[TreeNode]) -> None:
        """
        Perform in-order traversal and find the kth smallest element.
        
        Args:
            node: Current node being visited
        """
        if not node or self.result is not None:
            return
        
        # Traverse left subtree
        self.inorderTraversal(node.left)
        
        # Process current node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        
        # Traverse right subtree
        self.inorderTraversal(node.right)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solutionRecursive = SolutionRecursive()
    
    # Helper function to build tree from list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                leftIdx = 2 * i + 1
                rightIdx = 2 * i + 2
                if leftIdx < len(nodes):
                    node.left = nodes[leftIdx]
                if rightIdx < len(nodes):
                    node.right = nodes[rightIdx]
        return nodes[0]
    
    # Test case 1
    root1 = build_tree([3, 1, 4, None, 2])
    k1 = 1
    print(f"Input: root = [3,1,4,null,2], k = {k1}")
    print(f"Output (Iterative): {solution.kthSmallest(root1, k1)}")
    root1 = build_tree([3, 1, 4, None, 2])  # Rebuild for recursive
    print(f"Output (Recursive): {solutionRecursive.kthSmallest(root1, k1)}")
    print(f"Expected: 1")
    print()
    
    # Test case 2
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    k2 = 3
    print(f"Input: root = [5,3,6,2,4,null,null,1], k = {k2}")
    print(f"Output (Iterative): {solution.kthSmallest(root2, k2)}")
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])  # Rebuild for recursive
    print(f"Output (Recursive): {solutionRecursive.kthSmallest(root2, k2)}")
    print(f"Expected: 3")
    print()
    
    # Test case 3
    root3 = build_tree([1])
    k3 = 1
    print(f"Input: root = [1], k = {k3}")
    print(f"Output (Iterative): {solution.kthSmallest(root3, k3)}")
    root3 = build_tree([1])  # Rebuild for recursive
    print(f"Output (Recursive): {solutionRecursive.kthSmallest(root3, k3)}")
    print(f"Expected: 1")
