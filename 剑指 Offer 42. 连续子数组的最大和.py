class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划-原地修改
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)