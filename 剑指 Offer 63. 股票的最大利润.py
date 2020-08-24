class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #动态规划 优化
        minprice, maxprofit = float('inf'), 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit