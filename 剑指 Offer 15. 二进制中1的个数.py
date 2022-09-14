class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. 逐位判断 O(logn) O(1)
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

        # # 2. 位运算 n&n-1消除末尾1 O(M) O(1)
        # count = 0
        # while n:
        #     count += 1
        #     n &= n - 1
        # return count

        # # 3. bin
        # return bin(n).count('1')