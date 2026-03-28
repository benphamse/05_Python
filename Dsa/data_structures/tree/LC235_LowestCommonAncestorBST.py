"""
LeetCode Problem #235: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given 
nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself)."

Algorithm: Iterative traversal using BST properties
Time Complexity: O(h) where h is the height of the tree
Space Complexity: O(1) - constant space
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor of two nodes in a BST.
        
        Uses BST property: left subtree < root < right subtree
        
        Args:
            root: Root of the binary search tree
            p: First node
            q: Second node
        
        Returns:
            The lowest common ancestor node
        """
        while True:
            # If both p and q are smaller than root, LCA must be in left subtree
            if root.val > p.val and root.val > q.val:
                root = root.left
            # If both p and q are larger than root, LCA must be in right subtree
            elif root.val < p.val and root.val < q.val:
                root = root.right
            # If p and q are on different sides (or one equals root), root is the LCA
            else:
                return root


class SolutionRecursive:
    """Alternative recursive solution"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursive approach to find LCA in BST.
        
        Args:
            root: Root of the binary search tree
            p: First node
            q: Second node
        
        Returns:
            The lowest common ancestor node
        """
        # If both nodes are smaller, go left
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both nodes are larger, go right
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Current node is the LCA
        else:
            return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_recursive = SolutionRecursive()
    
    # Test case 1: LCA of 2 and 8 is 6
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    
    p1 = root1.left  # Node 2
    q1 = root1.right  # Node 8
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    print(f"Test case 1 (Iterative):")
    print(f"Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8")
    print(f"Output: {result1.val}")
    print(f"Expected: 6")
    print()
    
    # Test case 2: LCA of 2 and 4 is 2
    p2 = root1.left  # Node 2
    q2 = root1.left.right  # Node 4
    result2 = solution.lowestCommonAncestor(root1, p2, q2)
    print(f"Test case 2 (Iterative):")
    print(f"Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4")
    print(f"Output: {result2.val}")
    print(f"Expected: 2")
    print()
    
    # Test case 3: Simple tree with recursive solution
    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    p3 = root3
    q3 = root3.left
    result3 = solution_recursive.lowestCommonAncestor(root3, p3, q3)
    print(f"Test case 3 (Recursive):")
    print(f"Input: root = [2,1], p = 2, q = 1")
    print(f"Output: {result3.val}")
    print(f"Expected: 2")
