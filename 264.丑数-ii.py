#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode.cn/problems/ugly-number-ii/description/
#
# algorithms
# Medium (58.79%)
# Likes:    968
# Dislikes: 0
# Total Accepted:    139.2K
# Total Submissions: 236.7K
# Testcase Example:  '10'
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # # 1. 动态规划 三指针 O(N) O(N)
        # dp = [1]*n
        # a = b = c = 0
        # for i in range(1, n):
        #     n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
        #     dp[i] = min(n2, n3, n5)
        #     if dp[i] == n2:
        #         a += 1
        #     if dp[i] == n3:
        #         b += 1
        #     if dp[i] == n5:
        #         c += 1
        # return dp[-1]

        # 2. 最小堆 O(NlogN) O(N)
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n):
            cur = heapq.heappop(heap)
            if i == n-1:
                return cur
            for factor in factors:
                tmp = cur * factor
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(heap, tmp)

# @lc code=end

