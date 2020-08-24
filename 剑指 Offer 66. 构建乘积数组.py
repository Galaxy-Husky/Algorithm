class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 双向遍历
        ''' if not a:
            return []
        L, R = [1], [1]
        n = len(a)
        for i in range(1, n):
            L.append(L[-1] * a[i-1])
        for i in range(n-2, -1, -1):
            R.insert(0, R[0] * a[i+1])
        res = [x * y for x, y in zip(L, R)]
        return res '''
        if not a:
            return []
        L = R = 1
        n = len(a)
        res = [0] * n
        for i in range(n):
            res[i] = L
            L *= a[i]
        for i in range(n-1, -1, -1):
            res[i] *= R
            R *= a[i]
        return res
