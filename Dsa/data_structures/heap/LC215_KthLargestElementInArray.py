"""
LeetCode Problem #215: Kth Largest Element in an Array
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Algorithm: Min Heap (Approach 1) or QuickSelect (Approach 2)
Time Complexity: O(N log k) for min heap, O(N) average for QuickSelect
Space Complexity: O(k) for min heap, O(1) for QuickSelect
"""

import heapq
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find kth largest element using min heap of size k.
        
        Similar to "Kth Largest Element in Stream" - maintain a min heap
        containing the k largest elements. The root is the kth largest.
        
        Args:
            nums: Array of integers
            k: Position of largest element to find (1-indexed)
        
        Returns:
            The kth largest element
        """
        # Min heap to store k largest elements
        minHeap = []
        
        for num in nums:
            if len(minHeap) < k:
                # Heap not full yet, add the number
                heapq.heappush(minHeap, num)
            elif num > minHeap[0]:
                # Current number is larger than smallest in k largest
                heapq.heapreplace(minHeap, num)
        
        # Root of min heap is the kth largest element
        return minHeap[0]
    
    def findKthLargestMaxHeap(self, nums: List[int], k: int) -> int:
        """
        Alternative: Use max heap and pop k times.
        
        Simpler but less efficient when k is small.
        Time: O(N + k log N), Space: O(N)
        
        Args:
            nums: Array of integers
            k: Position of largest element to find
        
        Returns:
            The kth largest element
        """
        # Convert to max heap (negate values)
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        
        # Pop k-1 times to get to kth largest
        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        
        # Return kth largest (negate back)
        return -maxHeap[0]
    
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        """
        Optimal approach using QuickSelect algorithm.
        
        QuickSelect is like QuickSort but only recurses into one partition.
        We're looking for the (n - k)th smallest element (== kth largest).
        
        Time: O(N) average, O(N²) worst case
        Space: O(1) excluding recursion stack
        
        Args:
            nums: Array of integers
            k: Position of largest element to find
        
        Returns:
            The kth largest element
        """
        def quickSelect(left: int, right: int, targetIdx: int) -> int:
            """Helper function to perform QuickSelect."""
            if left == right:
                return nums[left]
            
            # Random pivot for better average performance
            pivotIdx = random.randint(left, right)
            
            # Partition around pivot
            pivotIdx = partition(left, right, pivotIdx)
            
            # Check if we found the target
            if targetIdx == pivotIdx:
                return nums[targetIdx]
            elif targetIdx < pivotIdx:
                return quickSelect(left, pivotIdx - 1, targetIdx)
            else:
                return quickSelect(pivotIdx + 1, right, targetIdx)
        
        def partition(left: int, right: int, pivotIdx: int) -> int:
            """Partition array around pivot, return pivot's final position."""
            pivotValue = nums[pivotIdx]
            
            # Move pivot to end
            nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]
            
            # Move all smaller elements to left
            storeIdx = left
            for i in range(left, right):
                if nums[i] < pivotValue:
                    nums[i], nums[storeIdx] = nums[storeIdx], nums[i]
                    storeIdx += 1
            
            # Move pivot to its final position
            nums[storeIdx], nums[right] = nums[right], nums[storeIdx]
            return storeIdx
        
        # kth largest = (n - k)th smallest (0-indexed)
        n = len(nums)
        return quickSelect(0, n - 1, n - k)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output (MinHeap): {solution.findKthLargest(nums1.copy(), k1)}")
    print(f"Output (MaxHeap): {solution.findKthLargestMaxHeap(nums1.copy(), k1)}")
    print(f"Output (QuickSelect): {solution.findKthLargestQuickSelect(nums1.copy(), k1)}")
    print(f"Expected: 5")
    print()
    
    # Test case 2: Find largest (k=1)
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output (MinHeap): {solution.findKthLargest(nums2.copy(), k2)}")
    print(f"Output (MaxHeap): {solution.findKthLargestMaxHeap(nums2.copy(), k2)}")
    print(f"Output (QuickSelect): {solution.findKthLargestQuickSelect(nums2.copy(), k2)}")
    print(f"Expected: 4")
    print()
    
    # Test case 3: Single element
    nums3 = [1]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output (MinHeap): {solution.findKthLargest(nums3.copy(), k3)}")
    print(f"Expected: 1")
    print()
    
    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    k4 = 2
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output (MinHeap): {solution.findKthLargest(nums4.copy(), k4)}")
    print(f"Expected: -2")
    print()
    
    # Test case 5: Duplicates
    nums5 = [5, 5, 5, 5, 5]
    k5 = 3
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Output (MinHeap): {solution.findKthLargest(nums5.copy(), k5)}")
    print(f"Expected: 5")
