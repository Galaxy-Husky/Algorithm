#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (54.81%)
# Likes:    1155
# Dislikes: 0
# Total Accepted:    269.2K
# Total Submissions: 491.3K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 
# 注意：你不能在买入股票前卖出股票。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. 一次遍历 (动态规划优化) O(N) O(1)
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit

        # # 2. 动态规划 O(N) O(N)
        # n = len(prices)
        # if n == 0: 
        #     return 0
        # dp = [0] * n
        # min_price = prices[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1], prices[i] - min_price)
        #     min_price = min(min_price, prices[i])
        # return dp[-1]

# @lc code=end

