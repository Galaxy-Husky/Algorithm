class Solution:
    def sumNums(self, n: int) -> int:
        #逻辑运算符的短路效应
        # return n and n + self.sumNums(n - 1)
