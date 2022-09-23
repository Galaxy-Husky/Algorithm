class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 1. DFS O(MN) O(MN)

        # # 1.1 递归
        # def dfs(i, j, si, sj):
        #     if i >= m or j >= n or si + sj > k or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #     return 1+dfs(i+1, j, si+1 if (i+1) % 10 else si-8, sj)+dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj-8)
            
        # visited = set()
        # return dfs(0, 0, 0, 0)

        # # 1.2 循环递推
        # def get_sum(n):
        #     res = 0
        #     while n:
        #         res += n % 10
        #         n //= 10
        #     return res

        # visited = set([(0, 0)])
        # for i in range(m):
        #     for j in range(n):
        #         if ((i-1, j) in visited or (i, j-1) in visited) and get_sum(i) + get_sum(j) <= k:
        #             visited.add((i, j))
        # return len(visited)

        # 2. BFS O(MN) O(MN)
        q = [(0, 0, 0, 0)]
        visited = set()
        while q:
            i, j, si, sj = q.pop(0)
            if i >= m or j >= n or si + sj > k or (i, j) in visited:
                continue
            visited.add((i, j))
            q.append((i+1, j, si+1 if (i+1) % 10 else si-8, sj))
            q.append((i, j+1, si, sj+1 if (j+1) % 10 else sj-8))
        return len(visited)