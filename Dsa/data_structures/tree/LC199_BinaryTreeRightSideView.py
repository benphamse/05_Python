"""
LeetCode Problem #199: Binary Tree Right Side View
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.

Algorithm: BFS (Level Order Traversal)
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(w) where w is the maximum width of the tree
"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the right side view of binary tree using BFS.
        
        Args:
            root: Root of the binary tree
        
        Returns:
            List of values visible from right side
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            levelSize = len(queue)
            
            # Process all nodes at current level
            for i in range(levelSize):
                node = queue.popleft()
                
                # The last node at each level is visible from right side
                if i == levelSize - 1:
                    result.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: root = [1,2,3,null,5,null,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(f"Input: root = [1,2,3,null,5,null,4]")
    print(f"Output: {solution.rightSideView(root1)}")
    print(f"Expected: [1, 3, 4]")
    print(f"Explanation: Right side view shows 1, 3, 4")
    print()
    
    # Test case 2: root = [1,null,3]
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(f"Input: root = [1,null,3]")
    print(f"Output: {solution.rightSideView(root2)}")
    print(f"Expected: [1, 3]")
    print()
    
    # Test case 3: root = []
    root3 = None
    print(f"Input: root = []")
    print(f"Output: {solution.rightSideView(root3)}")
    print(f"Expected: []")
    print()
    
    # Test case 4: root = [1,2,3,4]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    print(f"Input: root = [1,2,3,4]")
    print(f"Output: {solution.rightSideView(root4)}")
    print(f"Expected: [1, 3, 4]")
    print(f"Explanation: From right side, we see 1, 3, and 4 (leftmost of deepest level)")
