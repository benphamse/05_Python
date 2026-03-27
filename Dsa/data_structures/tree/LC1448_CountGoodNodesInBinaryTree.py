"""
LeetCode Problem #1449: Count Good Nodes in Binary Tree
Difficulty: Medium
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Algorithm: DFS (Depth-First Search)
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height (recursion stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count good nodes in binary tree using DFS.
        
        Args:
            root: Root of the binary tree
        
        Returns:
            Number of good nodes in the tree
        """
        return self.dfs(root, root.val)
    
    def dfs(self, node: Optional[TreeNode], maxVal: int) -> int:
        """
        Helper method to traverse tree and count good nodes.
        
        Args:
            node: Current node being visited
            maxVal: Maximum value seen in path from root to current node
        
        Returns:
            Count of good nodes in subtree rooted at node
        """
        if not node:
            return 0
        
        # Current node is good if its value >= max value in path
        count = 1 if node.val >= maxVal else 0
        
        # Update max value for children
        newMaxVal = max(maxVal, node.val)
        
        # Count good nodes in left and right subtrees
        count += self.dfs(node.left, newMaxVal)
        count += self.dfs(node.right, newMaxVal)
        
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: root = [3,1,4,3,null,1,5]
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    print(f"Input: root = [3,1,4,3,null,1,5]")
    print(f"Output: {solution.goodNodes(root1)}")
    print(f"Expected: 4")
    print(f"Explanation: Nodes in blue are good (3, 4, 3, 5)")
    print()
    
    # Test case 2: root = [3,3,null,4,2]
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)
    print(f"Input: root = [3,3,null,4,2]")
    print(f"Output: {solution.goodNodes(root2)}")
    print(f"Expected: 3")
    print(f"Explanation: Root, left child (3), and left-left child (4) are good")
    print()
    
    # Test case 3: root = [1]
    root3 = TreeNode(1)
    print(f"Input: root = [1]")
    print(f"Output: {solution.goodNodes(root3)}")
    print(f"Expected: 1")
