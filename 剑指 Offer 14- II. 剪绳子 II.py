class Solution:
    def cuttingRope(self, n: int) -> int:
        # 数学-尽可能将绳子以长度3等分为多段时，乘积最大。
        # 大数求余

        '''if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        p = 1000000007
        if b == 0:
            return 3 ** a % p
        if b == 1:
            return 3 ** (a-1) * 4 % p
        return 3 ** a * 2 % p'''

        '''# 循环求余-(x^a) % p = [(x^(a-1) % p) * x] % p 
        def  remainder(x, a, p):
            rem = 1
            for _ in range(a):
                rem = (rem * x) % p
            return rem'''

        '''# 快速幂求余
        # a为奇数：(x^a) % p = [(x^2 % p)^(a//2) * x] % p 
        # a为偶数：(x^a) % p = (x^2 % p)^(a//2)
        def remainder(x, a, p):
            rem = 1
            while a > 0:
                if a % 2:
                    rem = (rem * x) % p
                x = x ** 2 % p
                a //= 2
            return rem'''

        if n <= 3:
            return n - 1
        a, b = n // 3 - 1, n % 3
        p = 1000000007
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
        return (rem * 2 * 3) % p
        

