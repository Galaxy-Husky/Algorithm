class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # 1. range O(10^n) O(1)
        return list(range(1, 10 ** n))

        # 2. 大数加法 -> 字符串