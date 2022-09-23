class Solution:
    def twoSum(self, n: int) -> List[float]:
        # 1. 动态规划 O(N^2) O(N)
        dp = [1/6] * 6
        for i in range(2, n+1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k] += dp[j] / 6
            dp = tmp
        return dp