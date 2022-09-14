class Solution:
    def fib(self, n: int) -> int:
        # 1. 动态规划

        if n < 2:
            return n

        # # 1.1
        # dp = [0, 1]
        # for i in range(2, n+1):
        #     dp.append((dp[i-1] + dp[i-2]) % 1000000007)
        # return dp[n]

        # 1.2 优化 O(N) O(1)
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b % (10 ** 9 + 7)