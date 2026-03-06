class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
		Find the missing number in the array using bitwise XOR.

		Args:
			nums: List of integers from 0 to n with one missing
		Returns:
			The missing number
		"""
		missing = len(nums)  # Start with n, since numbers are from 0 to n
		for i in range(len(nums)):
			missing ^= i ^ nums[i]  # XOR with index and value
		return missing