class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """ # 字符串切片s
        return s[n:] + s[:n] """

        '''# 列表遍历拼接
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)'''

        # 取余简化
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)
        
        """ # 三次反转
        arr = list(s)
        arr[:n] = arr[:n][::-1]
        arr[n:] = arr[n:][::-1]
        arr[:] = arr[::-1]
        return ''.join(arr)"""
