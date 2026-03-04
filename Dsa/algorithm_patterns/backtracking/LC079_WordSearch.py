"""
LeetCode Problem #79: Word Search
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Algorithm: Backtracking with DFS
Time Complexity: O(m * n * 4^L) - where L is length of word, 4 directions at each step
Space Complexity: O(L) - recursion depth for word length
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if word exists in board using backtracking.

        Args:
            board: 2D grid of characters
            word: Target word to find

        Returns:
            True if word exists in board, False otherwise
        """
        if not board or not board[0] or not word:
            return False

        rows = len(board)
        cols = len(board[0])
        
        # Try starting from each cell
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    # Mark as visited by changing the cell value
                    if self.backtrack(board, word, row, col, 0, rows, cols):
                        return True
        
        return False

    def backtrack(self, board: List[List[str]], word: str, row: int, col: int, 
                  index: int, rows: int, cols: int) -> bool:
        """
        Explore board using backtracking to find word.

        Args:
            board: 2D grid of characters (modified in-place for visited tracking)
            word: Target word to find
            row: Current row position
            col: Current column position
            index: Current index in word being matched
            rows: Total number of rows
            cols: Total number of columns

        Returns:
            True if word can be formed from current position, False otherwise
        """
        # Base case: found complete word
        if index == len(word):
            return True

        # Check bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        # Check if current cell matches and hasn't been visited
        if board[row][col] != word[index]:
            return False

        # Mark as visited by temporarily changing the value
        temp = board[row][col]
        board[row][col] = '#'

        # Approach 1: Direct calls with or chain
        # found = (
        #     self.backtrack(board, word, row - 1, col, index + 1, rows, cols) or  # up
        #     self.backtrack(board, word, row + 1, col, index + 1, rows, cols) or  # down
        #     self.backtrack(board, word, row, col - 1, index + 1, rows, cols) or  # left
        #     self.backtrack(board, word, row, col + 1, index + 1, rows, cols)     # right
        # )

        # Approach 2: Using 1D direction array (compact trick)
        # directions = [0, 1, 0, -1, 0]  # right, down, left, up
        # found = False
        # for i in range(4):
        #     newRow = row + directions[i]
        #     newCol = col + directions[i + 1]
        #     if self.backtrack(board, word, newRow, newCol, index + 1, rows, cols):
        #         found = True
        #         break

        # Approach 3: Using 2D direction array (more readable)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        found = False
        for dr, dc in directions:
            newRow = row + dr
            newCol = col + dc
            if self.backtrack(board, word, newRow, newCol, index + 1, rows, cols):
                found = True
                break

        # Backtrack: restore original value
        board[row][col] = temp

        return found


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word1 = "ABCCED"
    print(f"Input: board = {board1}")
    print(f"       word = '{word1}'")
    print(f"Output: {solution.exist(board1, word1)}")
    print(f"Expected: True")
    print()

    # Test case 2
    board2 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word2 = "SEE"
    print(f"Input: board = {board2}")
    print(f"       word = '{word2}'")
    print(f"Output: {solution.exist(board2, word2)}")
    print(f"Expected: True")
    print()

    # Test case 3
    board3 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word3 = "ABCB"
    print(f"Input: board = {board3}")
    print(f"       word = '{word3}'")
    print(f"Output: {solution.exist(board3, word3)}")
    print(f"Expected: False")
    print()

    # Test case 4
    board4 = [["a"]]
    word4 = "a"
    print(f"Input: board = {board4}")
    print(f"       word = '{word4}'")
    print(f"Output: {solution.exist(board4, word4)}")
    print(f"Expected: True")
