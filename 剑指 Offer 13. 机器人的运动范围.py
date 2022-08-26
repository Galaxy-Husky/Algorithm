class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 仅通过向右和向下移动，访问所有可达解

        # DFS
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < (si + sj) or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j, si+1 if (i+1) % 10 else si - 8, sj) + dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj -8)

        visited = set()
        return dfs(0, 0, 0, 0)

        '''def dfs(i, j, si, sj):
            if i >= m or j >= n or k < (si + sj) or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i+1, j, si+1 if (i+1) % 10 else si - 8, sj)
            dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj -8)

        visited = set()
        dfs(0, 0, 0, 0)
        return len(visited)'''

        '''# BFS-队列
        q = [(0, 0, 0, 0)]
        visited = set()
        while q:
            i, j, si, sj = q.pop(0)
            if i >= m or j >= n or k < (si + sj) or (i, j) in visited:
                continue
            visited.add((i, j))
            q.append((i+1, j, si+1 if (i+1) % 10 else si - 8, sj))
            q.append((i, j+1, si, sj+1 if (j+1) % 10 else sj -8))
        return len(q)'''
