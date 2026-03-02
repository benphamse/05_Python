"""
LeetCode Problem #40: Combination Sum II
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used ONCE in the combination.

Note: The solution set must not contain duplicate combinations.

Algorithm: Backtracking with duplicate handling
Time Complexity: O(2^n) - worst case, each element can be included or excluded
Space Complexity: O(n) - recursion depth
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations that sum to target (each number used once).

        Args:
            candidates: List of integers (may contain duplicates)
            target: Target sum

        Returns:
            List of all unique combinations that sum to target
        """
        result: List[List[int]] = []
        candidates.sort()  # Sort to handle duplicates
        self.backtrack(candidates, [], result, target, 0)
        return result

    def backtrack(self, candidates: List[int], current: List[int], 
                  result: List[List[int]], remain: int, idx: int) -> None:
        """
        Build combinations by trying each candidate once.

        Args:
            candidates: Sorted list of candidate numbers
            current: Current combination being built
            result: Accumulator for all valid combinations
            remain: Remaining sum needed to reach target
            idx: Current starting index
        """
        # Base case: exceeded target (pruning)
        if remain < 0:
            return

        # Base case: found valid combination
        if remain == 0:
            result.append(current[:])
            return

        # Try each candidate starting from idx
        for i in range(idx, len(candidates)):
            # Skip duplicates: if same as previous at same level, skip it
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            
            # Early termination: if current > remain, all next will be > remain (sorted)
            if candidates[i] > remain:
                break

            # Include candidates[i]
            current.append(candidates[i])
            # Move to next index (i+1) since each number can only be used once
            self.backtrack(candidates, current, result, remain - candidates[i], i + 1)
            # Backtrack: remove last element
            current.pop()


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {solution.combinationSum2(candidates1, target1)}")
    print(f"Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]")
    print()

    # Test case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {solution.combinationSum2(candidates2, target2)}")
    print(f"Expected: [[1, 2, 2], [5]]")
    print()

    # Test case 3
    candidates3 = [1]
    target3 = 1
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {solution.combinationSum2(candidates3, target3)}")
    print(f"Expected: [[1]]")
