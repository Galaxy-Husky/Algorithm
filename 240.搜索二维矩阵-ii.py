#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (39.47%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    47.4K
# Total Submissions: 120.2K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target = 5，返回 true。
# 
# 给定 target = 20，返回 false。
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Z字形查找 左下角or右上角 O(m+n) O(1)
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            n = matrix[i][j]
            if n == target:
                return True
            if n < target:
                j += 1
            if n > target:
                i -= 1
        return False
        
# @lc code=end

