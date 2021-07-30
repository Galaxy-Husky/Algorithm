class Solution:
    def hammingWeight(self, n: int) -> int:
        '''# 逐位判断
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count'''

        # 位运算
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count