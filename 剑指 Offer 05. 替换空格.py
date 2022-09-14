class Solution:
    def replaceSpace(self, s: str) -> str:
        # # 1. replace
        # return s.replace(' ', '%20')

        # 2. 遍历 O(N) O(N)
        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else:
                res.append(c)
        return ''.join(res)