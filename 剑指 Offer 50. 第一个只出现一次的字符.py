class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in s:
            if d[c] == 1:
                return c
        return ' '