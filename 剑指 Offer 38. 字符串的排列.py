class Solution:
    def permutation(self, s: str) -> List[str]:
        # 1. 回溯

        n = len(s) 
        res = []
        c = list(s)

        # # 1.1 交换+集合排除重复字符 O(N!N) O(N^2)

        # def dfs(x):
        #     if x == n - 1:
        #         res.append(''.join(c))
        #         return
            
        #     visited = set()
        #     for i in range(x, len(c)):
        #         if c[i] in visited:
        #             continue
        #         visited.add(c[i])
        #         c[i], c[x] = c[x], c[i]
        #         dfs(x+1)
        #         c[x], c[i] = c[i], c[x]
        
        # dfs(0)
        # return res

        # 1.2 排序 O(N!N) O(N)
        c.sort()
        visited = [0]*n

        def dfs(perm):
            if len(perm) == n:
                res.append(perm)
                return

            for i in range(n):
                if visited[i] or (i > 0 and not visited[i-1] and c[i] == c[i-1]):
                    continue
                visited[i] = 1
                dfs(perm+c[i])
                visited[i] = 0
        
        dfs('')
        return res
            
            

