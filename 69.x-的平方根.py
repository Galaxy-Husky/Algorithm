#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.53%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    102.5K
# Total Submissions: 272.6K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            num = mid ** 2
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

