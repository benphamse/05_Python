"""
LeetCode Problem #200: Number of Islands
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Algorithm: DFS (Depth-First Search) / Graph Traversal
Time Complexity: O(m * n) where m = rows, n = cols
Space Complexity: O(m * n) worst case for recursion stack
"""

from typing import List


class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands using DFS to mark visited cells.
        
        Args:
            grid: 2D grid of '1' (land) and '0' (water)
        
        Returns:
            Number of islands found
        """
        if not grid or not grid[0]:
            return 0
        
        self.m, self.n = len(grid), len(grid[0])
        count = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    
    def dfs(self, grid, i, j):
        """Mark current cell and recursively mark connected land cells."""
        grid[i][j] = '0'
        
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.m and 0 <= nj < self.n and grid[ni][nj] == '1':
                self.dfs(grid, ni, nj)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Multiple islands
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Input: grid with multiple connected lands")
    print(f"Output: {solution.numIslands(grid1)}")
    print(f"Expected: 1")
    print()
    
    # Test case 2: Multiple separate islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Input: grid with 3 separate islands")
    print(f"Output: {solution.numIslands(grid2)}")
    print(f"Expected: 3")
    print()
    
    # Test case 3: All water
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    print(f"Input: grid with all water")
    print(f"Output: {solution.numIslands(grid3)}")
    print(f"Expected: 0")
    print()
    
    # Test case 4: All land
    grid4 = [
        ["1","1"],
        ["1","1"]
    ]
    print(f"Input: grid with all land")
    print(f"Output: {solution.numIslands(grid4)}")
    print(f"Expected: 1")
