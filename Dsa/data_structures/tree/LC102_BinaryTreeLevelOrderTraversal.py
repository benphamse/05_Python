"""
LeetCode Problem #102: Binary Tree Level Order Traversal
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Algorithm: BFS (Breadth-First Search) using Queue
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(w) where w is the maximum width of the tree (max nodes at any level)
"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal of a binary tree.
        
        Args:
            root: Root of the binary tree
        
        Returns:
            List of lists containing node values at each level
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            levelSize = len(queue)
            currentLevel = []
            
            # Process all nodes at current level
            for _ in range(levelSize):
                node = queue.popleft()
                currentLevel.append(node.val)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(currentLevel)
        
        return result


class SolutionRecursive:
    """Alternative recursive DFS solution"""
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level order traversal using recursive DFS.
        
        Args:
            root: Root of the binary tree
        
        Returns:
            List of lists containing node values at each level
        """
        self.result = []
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node: Optional[TreeNode], level: int) -> None:
        """
        Helper method for DFS traversal.
        
        Args:
            node: Current node
            level: Current level depth
        """
        if not node:
            return
        
        # Create new level list if needed
        if level == len(self.result):
            self.result.append([])
        
        # Add current node to its level
        self.result[level].append(node.val)
        
        # Recursively process children
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solutionRecursive = SolutionRecursive()
    
    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(f"Test case 1 (BFS):")
    print(f"Input: root = [3,9,20,null,null,15,7]")
    print(f"Output: {solution.levelOrder(root1)}")
    print(f"Expected: [[3], [9, 20], [15, 7]]")
    print()
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    print(f"Test case 2 (BFS):")
    print(f"Input: root = [1]")
    print(f"Output: {solution.levelOrder(root2)}")
    print(f"Expected: [[1]]")
    print()
    
    # Test case 3: Empty tree
    root3 = None
    print(f"Test case 3 (BFS):")
    print(f"Input: root = []")
    print(f"Output: {solution.levelOrder(root3)}")
    print(f"Expected: []")
    print()
    
    # Test case 4: Using recursive solution
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    
    print(f"Test case 4 (DFS Recursive):")
    print(f"Input: root = [1,2,3,4,5]")
    print(f"Output: {solutionRecursive.levelOrder(root4)}")
    print(f"Expected: [[1], [2, 3], [4, 5]]")
