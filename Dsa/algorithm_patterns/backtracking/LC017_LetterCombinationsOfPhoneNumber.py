"""
LeetCode Problem #17: Letter Combinations of a Phone Number
Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Algorithm: Backtracking
Time Complexity: O(4^n * n) - where n is length of digits, 4 is max letters per digit
Space Complexity: O(n) - recursion depth
"""

from typing import List


class Solution:
    def __init__(self):
        self.digitToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all letter combinations using backtracking.

        Args:
            digits: String of digits from 2-9

        Returns:
            List of all possible letter combinations
        """
        if not digits:
            return []

        result: List[str] = []
        self.backtrack("", result, 0, digits)
        return result

    def backtrack(self, current: str, result: List[str], index: int, digits: str) -> None:
        """
        Build letter combinations by choosing letters for each digit.

        Args:
            current: Current combination being built
            result: Accumulator for all valid combinations
            index: Current digit index
            digits: Original digits string
        """
        # Base case: processed all digits
        if index == len(digits):
            result.append(current)
            return

        # Get letters for current digit
        letters = self.digitToLetters[digits[index]]

        # Try each letter
        for letter in letters:
            self.backtrack(current + letter, result, index + 1, digits)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    digits1 = "23"
    print(f"Input: digits = '{digits1}'")
    print(f"Output: {solution.letterCombinations(digits1)}")
    print(f"Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']")
    print()

    # Test case 2
    digits2 = ""
    print(f"Input: digits = '{digits2}'")
    print(f"Output: {solution.letterCombinations(digits2)}")
    print(f"Expected: []")
    print()

    # Test case 3
    digits3 = "2"
    print(f"Input: digits = '{digits3}'")
    print(f"Output: {solution.letterCombinations(digits3)}")
    print(f"Expected: ['a', 'b', 'c']")
    print()

    # Test case 4
    digits4 = "79"
    print(f"Input: digits = '{digits4}'")
    print(f"Output: {solution.letterCombinations(digits4)}")
    print(f"Expected: ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']")
