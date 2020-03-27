class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 约瑟夫环 自底向上 迭代
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last 
        """ # 递归
        if n == 1:
            return 0
        return (self.lastRemaining(n-1, m) + m) % n """