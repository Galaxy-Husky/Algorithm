class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1. 密码锁规律 O(log10^N) O(1)
        res = 0
        digit = 1
        high, cur, low = n // 10, n % 10, 0
        while high or cur:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res