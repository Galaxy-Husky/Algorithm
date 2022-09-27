class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划 O(MN) O(MN)
        m, n = len(s), len(p)
        dp  = [[False] * (n+1) for _ in range (m+1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n+1):
                if  p[j-1] != '*':
                    if i > 0 and (p[j-1] == '.' or s[i-1] == p[j-1]):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    if j < 2:
                        continue
                    dp[i][j] = dp[i][j-2]
                    if i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] |= dp[i-1][j]
        return dp[-1][-1]