class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        pre = cur = 0
        for n in nums:
            temp = max(n + pre, cur)
            pre = cur
            cur = temp
        return cur

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))