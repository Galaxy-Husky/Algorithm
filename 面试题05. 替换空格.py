import re
class Solution:
    def replaceSpace(self, s: str) -> str:
        """ # 直接替换
        return s.replace(' ', '%20') """
        """ # 正则
        return re.sub('\s', '%20', s) """
        # 列表
        alist = []
        for c in s:
            if c == ' ':
                alist.append('%20')
            else:
                alist.append(c)
        return ''.join(alist)