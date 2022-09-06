#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (74.10%)
# Likes:    1253
# Dislikes: 0
# Total Accepted:    220.6K
# Total Submissions: 297.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
# 
# 
# 
# 
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#

# @lc code=start
from lib2to3.pgen2.token import RIGHTSHIFT


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length

        # # 1. 左右乘积
        # L, R = [0] * length, [0] * length
        # L[0] = 1
        # for i in range(1, length):
        #     L[i] = L[i-1] * nums[i-1]
        # R[length-1] = 1 
        # for i in range(length-2, -1, -1):
        #     R[i] = R[i+1] * nums[i+1]
        # for i in range(length):
        #     ans[i] = L[i] * R[i]
        # return ans

        # 2. 空间复杂度O(1)

        # # 2.1 两个循环
        # ans[0] = 1
        # for i in range(1, length):
        #     ans[i] = nums[i-1] * ans[i-1]
        # R = 1
        # for i in range(length-1, -1, -1):
        #     ans[i] *= R
        #     R *= nums[i]
        # return ans

        # 2.2 一个循环
        left = right = 1
        for i in range(length):
            ans[i] *= left
            left *= nums[i]
            ans[-1-i] *= right
            right *= nums[-1-i]
        return ans 
            


# @lc code=end

