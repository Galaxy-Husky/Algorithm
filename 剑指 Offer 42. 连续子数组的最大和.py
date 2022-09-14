class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. 动态规划
        length = len(nums)
        if not nums:
            return 0

        # # 1.1 O(N) O(N)
        # dp = [0] * length
        # dp[0] = nums[0]
        # for i in range(1, length):
        #     if dp[i-1] > 0:
        #         dp[i] = dp[i-1] + nums[i]
        #     else:
        #         dp[i] = nums[i]
        # return max(dp)

        # # 1.2 优化 O(N) O(1)
        # tmp = res = nums[0]
        # for i in range(1, length):
        #     tmp = max(nums[i], tmp+nums[i])
        #     res = max(tmp, res)
        # return res

        # 1.3 原地修改 O(N) O(1)
        for i in range(1, length):
            nums[i] += max(nums[i-1], 0)
        return max(nums)