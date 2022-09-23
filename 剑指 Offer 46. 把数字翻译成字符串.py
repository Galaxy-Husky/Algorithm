class Solution:
    def translateNum(self, num: int) -> int:
        # 1. 动态规划
        # dp[i] = dp[i-1] + dp[i-2]

        # # 1.1 转换字符串  O(N) O(N)
        # s = str(num)
        # a = b = 1
        # for i in range(2, len(s)+1):
        #     a, b = b, a+b if '10' <=s[i-2:i]<='25' else b
        # return b

        # 1.1 数字求余 反向 O(N) O(1)
        a = b = 1
        y = num % 10
        while num:
            num //= 10
            x = num % 10
            a, b = b, a+b if 10 <= 10*x + y<=25 else b
            y = x
        return b