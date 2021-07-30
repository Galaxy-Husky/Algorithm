class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 哈希表
        '''d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in s:
            if d[c] == 1:
                return c
        return ' ''''

        d = {}
        for c in s:
            d[c] = not c in d
        for c in s:
            if d[c]:
                return c
        return ' '
        