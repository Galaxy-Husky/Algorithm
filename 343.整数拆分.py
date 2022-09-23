#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (60.18%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    96.9K
# Total Submissions: 161.1K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # 尽可能将绳子以长度3等分为多段时，乘积最大。

        # 1. O(1) O(1)
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return 3 ** a
        if b == 1:
            return 3 ** (a-1) * 4
        if b == 2:
            return 3 ** a * 2

        # # 2. 动态规划 O(N^2) O(N)
        # dp = [0] * (n+1)
        # dp[2] = 1
        # for i in range(3, n+1):
        #     for j in range(1, i // 2 + 1):
        #         dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        # return dp[n]
        
# @lc code=end

