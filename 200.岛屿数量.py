#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (46.94%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    65.7K
# Total Submissions: 138.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给定一个由 '1'（陆地）和
# '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
# 
# 示例 1:
# 
# 输入:
# 11110
# 11010
# 11000
# 00000
# 
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# 11000
# 11000
# 00100
# 00011
# 
# 输出: 3
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # DFS O(MN) O(MN)
        # def dfs(i, j):
        #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        #         return
        #     grid[i][j] = '#'
        #     dfs(i+1, j)
        #     dfs(i-1, j)
        #     dfs(i, j+1)
        #     dfs(i, j-1)

        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             dfs(i, j)
        #             count += 1
        # return count

        # BFS O(MN) O(MN)
        def bfs(i, j):
            q = [(i, j)]
            while q:
                (i, j) = q.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '#'
                    q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count

# @lc code=end

