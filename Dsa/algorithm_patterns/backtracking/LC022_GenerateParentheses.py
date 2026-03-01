"""
LeetCode Problem #22: Generate Parentheses
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Algorithm: Backtracking
Time Complexity: O(4^n / sqrt(n)) - Catalan number, approximately 4^n / sqrt(n)
Space Complexity: O(n) - recursion depth
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid parentheses combinations using backtracking.

        Args:
            n: Number of pairs of parentheses

        Returns:
            List of all valid parentheses combinations
        """
        result: List[str] = []
        self.backtrack("", 0, 0, n, result)
        return result

    def backtrack(self, current: str, openCount: int, closeCount: int, 
                  n: int, result: List[str]) -> None:
        """
        Build valid parentheses by adding '(' or ')' based on constraints.

        Args:
            current: Current string being built
            openCount: Number of '(' added so far
            closeCount: Number of ')' added so far
            n: Target number of pairs
            result: Accumulator for all valid combinations
        """
        # Base case: reached maximum length (2n characters)
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add '(' if we haven't used all opening parentheses
        if openCount < n:
            self.backtrack(current + "(", openCount + 1, closeCount, n, result)

        # Add ')' if it won't make the string invalid (closeCount < openCount)
        if closeCount < openCount:
            self.backtrack(current + ")", openCount, closeCount + 1, n, result)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {solution.generateParenthesis(n1)}")
    print(f"Expected: ['((()))', '(()())', '(())()', '()(())', '()()()']")
    print()

    # Test case 2
    n2 = 1
    print(f"Input: n = {n2}")
    print(f"Output: {solution.generateParenthesis(n2)}")
    print(f"Expected: ['()']")
    print()

    # Test case 3
    n3 = 2
    print(f"Input: n = {n3}")
    print(f"Output: {solution.generateParenthesis(n3)}")
    print(f"Expected: ['(())', '()()']")
