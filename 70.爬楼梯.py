#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.82%)
# Likes:    838
# Dislikes: 0
# Total Accepted:    133.6K
# Total Submissions: 279.3K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. 动态规划 

        # # 1. O(N) O(N)
        # if n < 2:
        #     return 1
        # dp = [1, 1]
        # for i in range(2, n+1):
        #    dp.append((dp[i-1] + dp[i-2]))
        # return dp[-1]

        # 1.2 斐波那契 O(N) O(1)
        a = b = 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
        
# @lc code=end

