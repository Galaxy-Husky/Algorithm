class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂

        # 递归-自顶向下
        if n < 0 :
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        if n % 2:
            return half * half * x
        else:
            return half * half

