"""
LeetCode Problem #46: Permutations
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Algorithm: Backtracking
- Approach 1: Build permutation by selecting unused elements (uses membership check)
- Approach 2a: Swap approach with for loop - fix position start and swap with all positions
- Approach 2b: Swap approach without for loop - recursive iteration through swap positions

Time Complexity: O(n! * n) - n! permutations, each takes O(n) to copy
Space Complexity: O(n) - recursion depth
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations using backtracking.

        Args:
            nums: List of distinct integers

        Returns:
            List of all possible permutations
        """
        result: List[List[int]] = []
        # Choose one approach:
        # self.backtrackWithFor(nums, [], result)  # Approach 1: Build permutation with membership check
        self.backtrack(nums[:], 0, result)  # Approach 2a: Swap with for loop
        # self.backtrackNoFor(nums[:], 0, 0, result)  # Approach 2b: Swap without for loop
        return result

    def backtrackWithFor(self, nums: List[int], current: List[int], result: List[List[int]]) -> None:
        """
        Build permutations using for loop (Approach 1).

        Args:
            nums: Original list of integers
            current: Current permutation being built
            result: Accumulator for all valid permutations
        """
        # Base case: used all numbers
        if len(current) == len(nums):
            result.append(current[:])
            return

        # Try each number that hasn't been used yet
        for num in nums:
            if num in current:  # Skip if already used
                continue
            
            # Include num in current permutation
            current.append(num)
            self.backtrackWithFor(nums, current, result)
            # Backtrack: remove last element
            current.pop()

    def backtrack(self, nums: List[int], start: int, result: List[List[int]]) -> None:
        """
        Build permutations using swap approach with for loop (Approach 2a).

        Args:
            nums: Array being permuted (modified in-place)
            start: Current position to fix
            result: Accumulator for all valid permutations
        """
        # Base case: reached end, save current permutation
        if start == len(nums):
            result.append(nums[:])
            return

        # Try swapping start with each position from start to end
        for i in range(start, len(nums)):
            # Swap start with i
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse to fix next position
            self.backtrack(nums, start + 1, result)
            # Backtrack: swap back
            nums[start], nums[i] = nums[i], nums[start]

    def backtrackNoFor(self, nums: List[int], start: int, swapIdx: int, result: List[List[int]]) -> None:
        """
        Build permutations using swap approach without for loop (Approach 2b).

        Args:
            nums: Array being permuted (modified in-place)
            start: Current position to fix
            swapIdx: Current position to try swapping with
            result: Accumulator for all valid permutations
        """
        # Base case: tried all swap positions for current start
        if swapIdx >= len(nums):
            return

        # Swap start with swapIdx
        nums[start], nums[swapIdx] = nums[swapIdx], nums[start]
        
        # If this is the last position, save permutation
        if start == len(nums) - 1:
            result.append(nums[:])
        else:
            # Recurse to fix next position (start from start+1)
            self.backtrackNoFor(nums, start + 1, start + 1, result)
        
        # Backtrack: swap back
        nums[start], nums[swapIdx] = nums[swapIdx], nums[start]

        # Try next swap position
        self.backtrackNoFor(nums, start, swapIdx + 1, result)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.permute(nums1)}")
    print(f"Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]")
    print()

    # Test case 2
    nums2 = [0, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.permute(nums2)}")
    print(f"Expected: [[0, 1], [1, 0]]")
    print()

    # Test case 3
    nums3 = [1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.permute(nums3)}")
    print(f"Expected: [[1]]")
