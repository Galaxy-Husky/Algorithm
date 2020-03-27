class Solution:
    def twoSum(self, n: int) -> List[float]:
        # 动态规划 dp[n][j] += dp[n-1][j-i] 1<=i<=6
        """ # 二维数组
        dp = [[0] * (6*n + 1) for _ in range(n+1)]
        for j in range(1, 7):
            dp[1][j] = 1
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for cur in range(1, 7):
                    if j - cur < i- 1:
                        break
                    dp[i][j] += dp[i-1][j-cur]
        total = 6 ** n
        return [x/total for x in dp[n][n:]] """
        # 一维数组 记忆重复子问题
        dp = [0] * (6*n+1)
        for i in range(1, 7):
            dp[i] = 1
        for i in range(2, n+1):
            for j in range(6*i, i-1, -1):
                tmp = 0
                for cur in range(1, 7):
                    if j - cur < i - 1:
                        break
                    tmp += dp[j-cur] 
                dp[j] = tmp
        total = 6 ** n                                    
        return [x/total for x in dp[n:]]