class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 约瑟夫环 dp[i] = (dp[i-1] + m) % n

        # 1. 动态规划 O(N) O(1)
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last
        
        # # 2. 递归 O(N) O(N)
        # if n == 1:
        #     return 0
        # return (self.lastRemaining(n-1, m) + m) % n