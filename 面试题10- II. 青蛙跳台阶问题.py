class Solution:
    def numWays(self, n: int) -> int:
        ''' # 动态规划
        if n <= 1:
            return 1
        num_list = [1, 1]
        for i in range(2, n+1):
           num_list.append(num_list[-1] + num_list[-2])
        return num_list[-1] % 1000000007 '''

        # 斐波那契
        if n <= 1:
            return 1
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b % 1000000007