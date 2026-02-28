"""
LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Algorithm: Recursive Tree Construction with HashMap
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) for the hashmap and recursion stack
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct binary tree from preorder and inorder traversal arrays.
        
        Key insights:
        - First element in preorder is always the root
        - Find root in inorder to split left and right subtrees
        - Elements left of root in inorder = left subtree
        - Elements right of root in inorder = right subtree
        - Recursively build left and right subtrees
        
        Args:
            preorder: Preorder traversal array
            inorder: Inorder traversal array
        
        Returns:
            Root of the constructed binary tree
        """
        # Build hashmap for quick lookup of indices in inorder
        self.inorderMap = {val: idx for idx, val in enumerate(inorder)}
        self.preorderIndex = 0
        self.preorder = preorder
        
        return self.buildTreeHelper(0, len(inorder) - 1)
    
    def buildTreeHelper(self, left: int, right: int) -> Optional[TreeNode]:
        """
        Helper method to recursively build the tree.
        
        Args:
            left: Left boundary in inorder array
            right: Right boundary in inorder array
        
        Returns:
            Root node of the subtree
        """
        # Base case: no elements to construct the tree
        if left > right:
            return None
        
        # Get the current root value from preorder
        rootValue = self.preorder[self.preorderIndex]
        root = TreeNode(rootValue)
        
        # Move to next element in preorder
        self.preorderIndex += 1
        
        # Find the index of root in inorder to split left and right subtrees
        inorderIndex = self.inorderMap[rootValue]
        
        # Build left subtree (elements before root in inorder)
        root.left = self.buildTreeHelper(left, inorderIndex - 1)
        
        # Build right subtree (elements after root in inorder)
        root.right = self.buildTreeHelper(inorderIndex + 1, right)
        
        return root


class SolutionAlternative:
    """Alternative solution without using class variables"""
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct binary tree using slicing approach.
        
        Args:
            preorder: Preorder traversal array
            inorder: Inorder traversal array
        
        Returns:
            Root of the constructed binary tree
        """
        if not preorder or not inorder:
            return None
        
        # First element in preorder is the root
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        
        # Find root position in inorder
        inorderIndex = inorder.index(rootValue)
        
        # Split and recursively build subtrees
        # Left subtree: next elements in preorder, left side of root in inorder
        root.left = self.buildTree(
            preorder[1:inorderIndex + 1],
            inorder[:inorderIndex]
        )
        
        # Right subtree: remaining elements in preorder, right side of root in inorder
        root.right = self.buildTree(
            preorder[inorderIndex + 1:],
            inorder[inorderIndex + 1:]
        )
        
        return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solutionAlt = SolutionAlternative()
    
    # Helper function to print tree in level order
    def print_tree(root):
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
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    print(f"Input: preorder = {preorder1}, inorder = {inorder1}")
    tree1 = solution.buildTree(preorder1, inorder1)
    print(f"Output (HashMap): {print_tree(tree1)}")
    tree1_alt = solutionAlt.buildTree(preorder1, inorder1)
    print(f"Output (Slicing): {print_tree(tree1_alt)}")
    print(f"Expected: [3, 9, 20, None, None, 15, 7]")
    print()
    
    # Test case 2
    preorder2 = [-1]
    inorder2 = [-1]
    print(f"Input: preorder = {preorder2}, inorder = {inorder2}")
    tree2 = solution.buildTree(preorder2, inorder2)
    print(f"Output (HashMap): {print_tree(tree2)}")
    tree2_alt = solutionAlt.buildTree(preorder2, inorder2)
    print(f"Output (Slicing): {print_tree(tree2_alt)}")
    print(f"Expected: [-1]")
    print()
    
    # Test case 3
    preorder3 = [1, 2, 4, 5, 3, 6, 7]
    inorder3 = [4, 2, 5, 1, 6, 3, 7]
    print(f"Input: preorder = {preorder3}, inorder = {inorder3}")
    tree3 = solution.buildTree(preorder3, inorder3)
    print(f"Output (HashMap): {print_tree(tree3)}")
    tree3_alt = solutionAlt.buildTree(preorder3, inorder3)
    print(f"Output (Slicing): {print_tree(tree3_alt)}")
    print(f"Expected: [1, 2, 3, 4, 5, 6, 7]")
