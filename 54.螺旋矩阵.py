#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (39.15%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    47.2K
# Total Submissions: 120.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1. 控制边界 O(MN) O(1)
        if not matrix or not matrix[0]:
            return []
        res = []
        row, col = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while True:
            res.extend(matrix[top][j] for j in range(left, right + 1))
            top += 1
            if top > bottom:
                break
            res.extend(matrix[i][right] for i in range(top, bottom + 1))
            right -= 1
            if left > right:
                break
            res.extend(matrix[bottom][j] for j in range(right, left - 1, -1))
            bottom -= 1
            if top > bottom:
                break
            res.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
            left += 1
            if left > right:
                break
        return res
        
        # # 2. 删除第一行-逆时针旋转90度
        # res = []
        # while matrix:
        #     res.extend(matrix.pop(0))
        #     matrix = list(zip(*matrix))[::-1]
        # return res
# @lc code=end

