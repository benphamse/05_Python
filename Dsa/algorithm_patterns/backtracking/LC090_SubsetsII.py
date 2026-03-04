"""
LeetCode Problem #90: Subsets II
Difficulty: Medium
Link: https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets.
Return the solution in any order.

Algorithm: Backtracking with duplicate handling
Time Complexity: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
Space Complexity: O(n) - recursion depth, excluding output
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all unique subsets using backtracking.

        Args:
            nums: List of integers (may contain duplicates)

        Returns:
            List of all unique subsets
        """
        result: List[List[int]] = []
        nums.sort()  # Sort to handle duplicates
        # Choose one approach:
        self.backtrackWithFor(nums, 0, [], result)  # Approach 1: For loop
        # self.backtrack(nums, 0, [], result)  # Approach 2: Include/Skip without for
        return result

    def backtrackWithFor(self, nums: List[int], start: int, current: List[int], 
                         result: List[List[int]]) -> None:
        """
        Build subsets using for loop, skipping duplicates (Approach 1).

        Args:
            nums: Sorted list of integers
            start: Starting index for current exploration
            current: Current subset being built
            result: Accumulator for all valid subsets
        """
        # Every node in the decision tree is a valid subset
        result.append(current[:])

        for i in range(start, len(nums)):
            # Skip duplicates: if same as previous at same level, skip it
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            # Include nums[i] in the current subset
            current.append(nums[i])
            # Recurse with next index to avoid duplicates
            self.backtrackWithFor(nums, i + 1, current, result)
            # Backtrack: remove the last element
            current.pop()

    def backtrack(self, nums: List[int], index: int, current: List[int], 
                  result: List[List[int]]) -> None:
        """
        Build subsets using include/skip approach without for loop (Approach 2).

        Args:
            nums: Sorted list of integers
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

        # Choice 2: Skip nums[index] and all duplicates of it
        # Move index forward while we see the same value
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.backtrack(nums, index + 1, current, result)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 2]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.subsetsWithDup(nums1)}")
    print(f"Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]")
    print()

    # Test case 2
    nums2 = [0]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.subsetsWithDup(nums2)}")
    print(f"Expected: [[], [0]]")
    print()

    # Test case 3
    nums3 = [4, 4, 4, 1, 4]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.subsetsWithDup(nums3)}")
    print(f"Expected: [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]")
