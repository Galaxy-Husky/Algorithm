class Solution:
    def add(self, a: int, b: int) -> int:
        # 非进位和-异或；进位和-与+左移1位
        # 补码运算-输出前还原

        # 1. 位运算 O(1) O(1)
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        while b:
            a, b = a ^ b, (a & b) << 1 & mask
        return a if a < 0x80000000 else ~(a ^ mask)