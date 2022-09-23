class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 1. 左右乘积列表

        n = len(a)

        # # 1.1 O(N) O(N)
        # L, R = [1]*n, [1]*n
        # for i in range(1, n):
        #     L[i] = L[i-1] * a[i-1]
        # for i in range(n-2, -1, -1):
        #     R[i] = R[i+1] * a[i+1]
        # res = [x * y for x, y in zip(L, R)]
        # return res

        # 1.2 O(N) O(1)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * a[i-1]

        R = 1
        for i in range(n-1, -1, -1):
            res[i] *= R
            R *= a[i]
        return res
