"""
LeetCode Problem #39: Combination Sum
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

Algorithm: Backtracking with pruning
Time Complexity: O(n^(target/min)) - worst case when minimum element is 1
Space Complexity: O(target/min) - recursion depth
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all combinations that sum to target using backtracking.

        Args:
            candidates: List of distinct integers
            target: Target sum

        Returns:
            List of all unique combinations that sum to target
        """
        result: List[List[int]] = []
        # Choose one approach:
        # self.backtrackWithFor(candidates, target, 0, [], result)  # Approach 1: For loop
        self.backtrack(candidates, target, 0, [], result)  # Approach 2: Include/Skip
        return result

    def backtrackWithFor(self, candidates: List[int], remaining: int, start: int,
                         current: List[int], result: List[List[int]]) -> None:
        """
        Build combinations using for loop (Approach 1).

        Args:
            candidates: List of candidate numbers
            remaining: Remaining sum needed to reach target
            start: Starting index to avoid duplicate combinations
            current: Current combination being built
            result: Accumulator for all valid combinations
        """
        # Base case: found valid combination
        if remaining == 0:
            result.append(current[:])
            return

        # Base case: exceeded target (pruning)
        if remaining < 0:
            return

        # Try each candidate starting from 'start' index
        for i in range(start, len(candidates)):
            # Include candidates[i]
            current.append(candidates[i])
            # Can reuse same element, so pass 'i' not 'i+1'
            self.backtrackWithFor(candidates, remaining - candidates[i], i, current, result)
            # Backtrack: remove last element
            current.pop()

    def backtrack(self, candidates: List[int], remaining: int, index: int, 
                  current: List[int], result: List[List[int]]) -> None:
        """
        Build combinations by including or skipping each candidate.

        Args:
            candidates: List of candidate numbers
            remaining: Remaining sum needed to reach target
            index: Current index being decided
            current: Current combination being built
            result: Accumulator for all valid combinations
        """
        # Base case: found valid combination
        if remaining == 0:
            result.append(current[:])
            return

        # Base case: exceeded target or no more candidates
        if remaining < 0 or index >= len(candidates):
            return

        # Choice 1: Include candidates[index] (can reuse, so stay at index)
        current.append(candidates[index])
        self.backtrack(candidates, remaining - candidates[index], index, current, result)
        current.pop()

        # Choice 2: Skip candidates[index] (move to next)
        self.backtrack(candidates, remaining, index + 1, current, result)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {solution.combinationSum(candidates1, target1)}")
    print(f"Expected: [[2, 2, 3], [7]]")
    print()

    # Test case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {solution.combinationSum(candidates2, target2)}")
    print(f"Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]")
    print()

    # Test case 3
    candidates3 = [2]
    target3 = 1
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {solution.combinationSum(candidates3, target3)}")
    print(f"Expected: []")
