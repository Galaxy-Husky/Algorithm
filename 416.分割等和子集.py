#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (49.09%)
# Likes:    385
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 110K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 动态规划 01背包
        l = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [[False] * (target + 1) for _ in range(l + 1)]
        for i in range(l + 1):
            dp[i][0] = True
        for i in range(1, l + 1):
            for j in range(1, target + 1):
                if nums[i-1] == j:
                    dp[i][j] = True
                elif nums[i-1] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# @lc code=end

