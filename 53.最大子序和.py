#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (49.10%)
# Likes:    1701
# Dislikes: 0
# Total Accepted:    176.5K
# Total Submissions: 355.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # if nums:
        #     res = dp = nums[0]
        #     for i in range(1,len(nums)):
        #         dp = max(dp+nums[i], nums[i])
        #         res = max(res, dp)
        #     return res

        if nums:
            for i in range(1,len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
            return max(nums)
# @lc code=end

