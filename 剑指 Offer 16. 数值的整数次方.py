class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. 快速幂

        # # 1.1 递归 O(logn) O(logn)
        # if not n:
        #     return 1
        # if n < 0:
        #     return 1/self.myPow(x, -n)
        # half = self.myPow(x, n // 2)
        # if n % 2:
        #     return half * half * x
        # else:
        #     return half * half

        # 1.2 迭代 二进制 O(logn) O(1)
        res = 1
        if n < 0:
            x, n = 1/x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

