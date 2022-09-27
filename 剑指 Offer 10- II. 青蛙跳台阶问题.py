class Solution:
    def numWays(self, n: int) -> int:
        p = 10 ** 9 + 7

        # 1. 动态规划 

        # # 1. O(N) O(N)
        # if n < 2:
        #     return 1
        # dp = [1, 1]
        # for i in range(2, n+1):
        #    dp.append((dp[i-1] + dp[i-2]) % p)
        # return dp[-1]

        # 1.2 斐波那契 O(N) O(1)
        a, b = 1, 1
        for _ in range(2, n+1):
            s = (a + b) % p
            a = b
            b = s
        return b