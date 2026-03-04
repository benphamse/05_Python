"""
LeetCode Problem #78: Subsets
Difficulty: Medium
Link: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.
Return the solution in any order.

Algorithm: Backtracking
Time Complexity: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
Space Complexity: O(n) - recursion depth, excluding output
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets using backtracking.

        Args:
            nums: List of unique integers

        Returns:
            List of all possible subsets
        """
        result: List[List[int]] = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums: List[int], index: int, current: List[int], result: List[List[int]]) -> None:
        """
        Build subsets by choosing to include or skip each element.

        Args:
            nums: Original list of integers
            index: Current index being decided
            current: Current subset being built
            result: Accumulator for all valid subsets
        """
        # Base case: all elements have been decided
        if index == len(nums):
            result.append(current[:])
            return

        # Choice 1: Include nums[index]
        current.append(nums[index])
        self.backtrack(nums, index + 1, current, result)
        current.pop()

        # Choice 2: Skip nums[index]
        self.backtrack(nums, index + 1, current, result)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.subsets(nums1)}")
    print(f"Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]")
    print()

    # Test case 2
    nums2 = [0]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.subsets(nums2)}")
    print(f"Expected: [[], [0]]")
    print()

    # Test case 3
    nums3 = [1, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.subsets(nums3)}")
    print(f"Expected: [[], [1], [1, 2], [2]]")
