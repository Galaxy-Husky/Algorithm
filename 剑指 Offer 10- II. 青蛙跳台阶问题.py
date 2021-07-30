class Solution:
    def numWays(self, n: int) -> int:
        '''# 动态规划
        if n < 2:
            return 1
        dp = [1, 1]
        for i in range(2, n+1):
           dp.append((dp[i-1] + dp[i-2]) % 1000000007)
        return dp[n]'''

        # 斐波那契
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007