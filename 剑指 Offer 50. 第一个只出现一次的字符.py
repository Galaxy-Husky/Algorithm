class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 1. 哈希表

        # 1.1 O(N) O(1)
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in s:
            if d[c] == 1:
                return c
        return ' '

        # # 1.2 O(N) O(1)
        # d = {}
        # for c in s:
        #     d[c] = not c in d
        # for c in s:
        #     if d[c]:
        #         return c
        # return ' '
        