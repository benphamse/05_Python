"""
LeetCode Problem #287: Find the Duplicate Number
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Algorithm: Floyd's Cycle Detection (Tortoise and Hare)
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point in the cycle
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findDuplicate(nums1)}")  # Expected: 2
    print()
    
    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findDuplicate(nums2)}")  # Expected: 3
    print()
    
    # Test case 3
    nums3 = [1, 1]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findDuplicate(nums3)}")  # Expected: 1
