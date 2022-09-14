class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # # 1. 字符串切片s O(N) O(N)
        # return s[n:] + s[:n]

        # # 2. 列表遍历拼接 O(N) O(N)

        # # 2.1
        # res = []
        # for i in range(n, len(s)):
        #     res.append(s[i])
        # for i in range(n):
        #     res.append(s[i])
        # return ''.join(res)

        # # 2.2 取余简化
        # res = []
        # for i in range(n, n + len(s)):
        #     res.append(s[i % len(s)])
        # return ''.join(res)
        
        # 3. 三次反转 O(N) O(1)
        arr = list(s)
        arr[:n] = arr[:n][::-1]
        arr[n:] = arr[n:][::-1]
        arr[:] = arr[::-1]
        return ''.join(arr)
