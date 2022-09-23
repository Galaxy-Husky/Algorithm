class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        # 1. 递归+逻辑运算符的短路效应 O(N) O(N)

        # 1.1
        # return n and n + self.sumNums(n - 1)

        # 1.2
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
