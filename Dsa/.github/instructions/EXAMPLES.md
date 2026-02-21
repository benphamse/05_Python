# Template Fill-in Examples

## Example 1: Two Sum (Easy)

### Filled Template:

```python
"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Algorithm: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map.

        Args:
            nums: List of integers
            target: Target sum

        Returns:
            List of two indices
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")
    print(f"Expected: [0, 1]")
    print()

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")
    print(f"Expected: [1, 2]")
    print()

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")
    print(f"Expected: [0, 1]")
```

**File Location**: `algorithm_patterns/arrays_and_hashing/LC001_TwoSum.py`

---

## Example 2: Valid Palindrome (Easy)

### Filled Template:

```python
"""
LeetCode Problem #125: Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.

Algorithm: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is palindrome using two pointers.

        Args:
            s: Input string

        Returns:
            True if palindrome, False otherwise
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: s = '{s1}'")
    print(f"Output: {solution.isPalindrome(s1)}")
    print(f"Expected: True")
    print()

    # Test case 2
    s2 = "race a car"
    print(f"Input: s = '{s2}'")
    print(f"Output: {solution.isPalindrome(s2)}")
    print(f"Expected: False")
    print()

    # Test case 3
    s3 = " "
    print(f"Input: s = '{s3}'")
    print(f"Output: {solution.isPalindrome(s3)}")
    print(f"Expected: True")
```

**File Location**: `algorithm_patterns/two_pointers/LC125_ValidPalindrome.py`

---

## Example 3: Find Duplicate Number (Medium)

### Filled Template:

```python
"""
LeetCode Problem #287: Find the Duplicate Number
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive. There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space.

Algorithm: Floyd's Cycle Detection (Tortoise and Hare)
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find duplicate using Floyd's cycle detection algorithm.

        Args:
            nums: Array with one duplicate number

        Returns:
            The duplicate number
        """
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
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.findDuplicate(nums1)}")
    print(f"Expected: 2")
    print()

    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.findDuplicate(nums2)}")
    print(f"Expected: 3")
    print()

    # Test case 3
    nums3 = [1, 1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.findDuplicate(nums3)}")
    print(f"Expected: 1")
```

**File Location**: `algorithm_patterns/arrays_and_hashing/LC287_FindDuplicate.py`

---

## Example 4: Binary Search (Easy)

### Filled Template:

```python
"""
LeetCode Problem #704: Binary Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

Algorithm: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search on sorted array.

        Args:
            nums: Sorted array of integers
            target: Target value to find

        Returns:
            Index of target if found, -1 otherwise
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.search(nums1, target1)}")
    print(f"Expected: 4")
    print()

    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.search(nums2, target2)}")
    print(f"Expected: -1")
    print()

    # Test case 3
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.search(nums3, target3)}")
    print(f"Expected: 0")
```

**File Location**: `algorithm_patterns/binary_search/LC704_BinarySearch.py`

---

## Placeholder Reference Guide

| Placeholder             | Description                        | Example                                     |
| ----------------------- | ---------------------------------- | ------------------------------------------- |
| `{PROBLEM_NUMBER}`      | LeetCode problem number (3 digits) | `001`, `287`, `704`                         |
| `{PROBLEM_TITLE}`       | Full problem title                 | `Two Sum`, `Find Duplicate Number`          |
| `{PROBLEM_SLUG}`        | URL-friendly slug                  | `two-sum`, `find-duplicate-number`          |
| `{DIFFICULTY}`          | Easy/Medium/Hard                   | `Easy`, `Medium`, `Hard`                    |
| `{PROBLEM_DESCRIPTION}` | Brief problem statement            | See examples above                          |
| `{ALGORITHM_NAME}`      | Main algorithm/technique           | `Hash Map`, `Two Pointers`, `Binary Search` |
| `{TIME_COMPLEXITY}`     | Big O time                         | `O(n)`, `O(log n)`, `O(n²)`                 |
| `{SPACE_COMPLEXITY}`    | Big O space                        | `O(1)`, `O(n)`, `O(log n)`                  |
| `{METHOD_NAME}`         | Function name (camelCase)          | `twoSum`, `isPalindrome`, `search`          |
| `{PARAMETERS}`          | Method parameters                  | `nums: List[int], target: int`              |
| `{RETURN_TYPE}`         | Return type hint                   | `List[int]`, `bool`, `int`                  |
| `{IMPLEMENTATION}`      | Actual code implementation         | See examples above                          |
| `{TEST_CASE_X}`         | Test case setup                    | `nums1 = [2, 7, 11, 15]`                    |

---

## Category Mapping Examples

| Problem              | Number | Category            | Reasoning                |
| -------------------- | ------ | ------------------- | ------------------------ | ------------- |
| Two Sum              | 1      | arrays_and_hashing  | Uses hash map            |
| Add Two Numbers      | 2      | linked_list         | Linked list manipulation |
| Longest Substring    | 3      | sliding_window      | Variable window          |
| Container Most Water | 11     | two_pointers        | Left/right pointers      |
| Valid Parentheses    | 20     | stack               | Stack for matching       |
| Binary Search        | 704    | binary_search       | Classic binary search    |
| Invert Binary Tree   | 226    | trees               | Tree traversal           |
| Kth Largest          | 215    | heap_priority_queue | Heap operation           |
| Permutations         | 46     | backtracking        | Generate all combos      |
| Number of Islands    | 200    | graphs              | DFS/BFS on grid          |
| Climbing Stairs      | 70     | dynamic_programming | DP problem               |
| Jump Game            | 55     | greedy              | Greedy approach          | eap operation |
| Permutations         | 46     | backtracking        | Generate all combos      |
| Number of Islands    | 200    | graphs              | DFS/BFS on grid          |
| Climbing Stairs      | 70     | dynamic_programming | DP problem               |
| Jump Game            | 55     | greedy              | Greedy approach          |
