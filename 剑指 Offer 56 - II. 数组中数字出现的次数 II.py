class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # 1. 哈希表 O(N) O(N)
        # dic = {}
        # for n in nums:
        #     if n in dic:
        #         dic[n] += 1
        #     else:
        #         dic[n] = 1
        # for key, value in dic.items():
        #     if value == 1:
        #         return key

        # # 2. 有限状态自动机 O(N) O(1)
        # ones, twos = 0, 0
        # for num in nums:
        #     ones = (ones ^ num) & ~twos
        #     twos = (twos ^ num) & ~ones
        # return ones

        # 遍历统计 O(N) O(1)
        counts = [0] * 32
        for num in nums:
            for i in range(32):
                counts[i] += num & 1
                num >>= 1
        
        res = 0
        for i in range(32):
            res <<= 1
            res |= counts[-1-i] % 3
        return res