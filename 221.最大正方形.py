#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode.cn/problems/maximal-square/description/
#
# algorithms
# Medium (49.26%)
# Likes:    1293
# Dislikes: 0
# Total Accepted:    234.9K
# Total Submissions: 476.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_length = 0
        row, col = len(matrix), len(matrix[0])

        # 1. 动态规划

        # 1.1  O(MN) O(MN)
        # dp = [[0] * col for _ in range(row)]
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == '1':
        #             if i == 0 or j == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        #             max_length = max(max_length, dp[i][j])

        # 1.2 优化 O(MN) O(N)
        dp = [0] * col
        prev = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[j], prev = 1, dp[j]
                    else:
                        dp[j], prev = min(prev, dp[j-1], dp[j]) + 1, dp[j]
                    max_length = max(max_length, dp[j])
                else:
                    dp[j] = 0

        res = max_length ** 2
        return res

# @lc code=end

