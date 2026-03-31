class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(nums[i], maxProduct * nums[i])
            minProduct = min(nums[i], minProduct * nums[i])
            result = max(result, maxProduct)
        return result