#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (73.94%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    87.9K
# Total Submissions: 118.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # 1. 回溯
        # # 1.1 原地修改
        # def backtrack(start):
        #     if start == n:
        #         res.append(nums[:])
        #         return
        #     for i in range(start, n):
        #         nums[i], nums[start] = nums[start], nums[i]
        #         backtrack(start+1)
        #         nums[i], nums[start] = nums[start], nums[i]
        # res = []
        # n = len(nums)
        # backtrack(0)
        # return res

        # 1.2 新建数组
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path+[nums[i]])
        res = []
        dfs(nums, [])
        return res

        # # 2. python permutations
        # return list(permutations(nums))
# @lc code=end

