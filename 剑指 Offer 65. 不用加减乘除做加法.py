class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        while b:
            tmp = a ^ b
            b = (a & b) << 1 & mask
            a = tmp
        return a if a < 0x80000000 else ~(a ^ mask)