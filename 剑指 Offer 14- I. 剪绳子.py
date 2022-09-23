class Solution:
    def cuttingRope(self, n: int) -> int:
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

