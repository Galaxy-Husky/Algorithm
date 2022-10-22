#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode.cn/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (43.00%)
# Likes:    1821
# Dislikes: 0
# Total Accepted:    313.9K
# Total Submissions: 729.9K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 测试用例的答案是一个 32-位 整数。
# 
# 子数组 是数组的连续子序列。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # 1. 动态规划 O(N) O(1)
        # res = min_val = max_val = nums[0]
        # for num in nums[1:]:
        #     if num < 0:
        #         min_val, max_val = max_val, min_val
        #     max_val = max(max_val * num, num)
        #     min_val = min(min_val * num, num)

        #     res = max(res, max_val)
        # return res

        # 2. 负数个数 O(N) O(1)
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse_nums[i] *= reverse_nums[i-1] or 1
        return max(nums+reverse_nums)
# @lc code=end

