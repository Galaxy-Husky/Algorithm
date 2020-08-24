class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        high, digit, low, res = n, 1, 0, 0
        while high > 0:
            cur = high % 10
            high //= 10
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit 
            digit *= 10
        return res