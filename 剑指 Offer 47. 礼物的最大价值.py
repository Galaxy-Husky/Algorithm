class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 1. 动态规划 原地修改 O(MN) O(1)

        m, n = len(grid), len(grid[0])

        # # 1.1 
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j ==0:
        #             continue
        #         if i == 0:
        #             grid[i][j] += grid[i][j-1]
        #         elif j == 0:
        #             grid[i][j] += grid[i-1][j]
        #         else:
        #             grid[i][j] += max(grid[i][j-1], grid[i-1][j])
        # return grid[-1][-1]

        # 1.2 优化
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
