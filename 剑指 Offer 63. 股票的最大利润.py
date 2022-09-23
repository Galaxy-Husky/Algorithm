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