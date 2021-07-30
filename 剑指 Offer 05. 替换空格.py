class Solution:
    def replaceSpace(self, s: str) -> str:
        '''# replace
        return s.replace(' ', '%20')'''

        # 遍历
        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else:
                res.append(c)
        return ''.join(res)