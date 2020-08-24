
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 异或 + 分组
        res = 0
        for n in nums:
            res ^= n
        div = 1
        while res & div == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^=n
        return [a, b]
