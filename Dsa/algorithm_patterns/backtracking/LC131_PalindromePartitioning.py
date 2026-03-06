"""
LeetCode Problem #131: Palindrome Partitioning
Difficulty: Medium
Link: https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Algorithm: Backtracking
Time Complexity: O(n * 2^n) - 2^n possible partitions, each takes O(n) to check palindrome
Space Complexity: O(n) - recursion depth
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Generate all palindrome partitions using backtracking.

        Args:
            s: Input string

        Returns:
            List of all possible palindrome partitions
        """
        result: List[List[str]] = []
        # Choose one approach:
        self.backtrack(s, 0, [], result)  # Approach 1: With for loop
        # self.backtrackNoFor(s, 0, 1, [], result)  # Approach 2: Recursive without for loop
        return result

    def backtrack(self, s: str, start: int, current: List[str], result: List[List[str]]) -> None:
        """
        Build palindrome partitions using for loop (Approach 1).

        Args:
            s: Original string
            start: Starting index for current exploration
            current: Current partition being built
            result: Accumulator for all valid partitions
        """
        # Base case: reached end of string
        if start == len(s):
            result.append(current[:])
            return

        # Try all possible end positions from start
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            # Only continue if current substring is palindrome
            if self.isPalindrome(substring):
                current.append(substring)
                self.backtrack(s, end + 1, current, result)
                current.pop()

    def backtrackNoFor(self, s: str, start: int, length: int, current: List[str], 
                       result: List[List[str]]) -> None:
        """
        Build palindrome partitions by trying all valid cuts.

        Args:
            s: Original string
            start: Starting index for current exploration
            current: Current partition being built
            result: Accumulator for all valid partitions
        """
        # Base case: reached end of string
        if start == len(s):
            result.append(current[:])
            return

        # Try all possible end positions from start
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            # Only continue if current substring is palindrome
            if self.isPalindrome(substring):
                current.append(substring)
                self.backtrack(s, end + 1, current, result)
                current.pop()

    def backtrackNoFor(self, s: str, start: int, length: int, current: List[str], 
                       result: List[List[str]]) -> None:
        """
        Build palindrome partitions recursively without for loop (Approach 2).

        Args:
            s: Original string
            start: Starting index for current exploration
            length: Current length of substring to try
            current: Current partition being built
            result: Accumulator for all valid partitions
        """
        # Base case: reached end of string
        if start == len(s):
            result.append(current[:])
            return

        # Base case: length exceeds remaining string
        if start + length > len(s):
            return

        # Try substring of current length
        substring = s[start:start + length]
        if self.isPalindrome(substring):
            # Include this palindrome and move to next position
            current.append(substring)
            self.backtrackNoFor(s, start + length, 1, current, result)
            current.pop()

        # Try next length at same position
        self.backtrackNoFor(s, start, length + 1, current, result)

    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is palindrome.

        Args:
            s: String to check

        Returns:
            True if palindrome, False otherwise
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "aab"
    print(f"Input: s = '{s1}'")
    print(f"Output: {solution.partition(s1)}")
    print(f"Expected: [['a', 'a', 'b'], ['aa', 'b']]")
    print()

    # Test case 2
    s2 = "a"
    print(f"Input: s = '{s2}'")
    print(f"Output: {solution.partition(s2)}")
    print(f"Expected: [['a']]")
    print()

    # Test case 3
    s3 = "aabb"
    print(f"Input: s = '{s3}'")
    print(f"Output: {solution.partition(s3)}")
    print(f"Expected: [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]")
