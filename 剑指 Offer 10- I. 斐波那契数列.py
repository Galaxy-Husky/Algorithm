class Solution:
    def fib(self, n: int) -> int:
        '''# 动态规划
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append((dp[i-1] + dp[i-2]) % 1000000007)
        return dp[n]'''

    # 优化
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a % 1000000007