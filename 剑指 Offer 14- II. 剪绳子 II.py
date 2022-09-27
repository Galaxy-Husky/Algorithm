class Solution:
    def cuttingRope(self, n: int) -> int:
        # 尽可能将绳子以长度3等分为多段时，乘积最大。

        # 1. 快速幂求余 O(logN) O(1)
        if n <= 3:
            return n - 1

        p = 1000000007
        a, b = n // 3-1, n % 3
        x, rem = 3, 1
        while a > 0:
            if a % 2:
                rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0:
            return (rem * 3) % p
        if b == 1:
            return (rem * 4) % p
        return (rem * 3 * 2) % p
