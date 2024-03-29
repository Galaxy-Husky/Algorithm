#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.62%)
# Likes:    1734
# Dislikes: 0
# Total Accepted:    293.8K
# Total Submissions: 869.5K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        min_value, max_value = -2**31, 2**31-1
        res = 0
        while x:
            if res > max_value // 10 or res < min_value // 10 + 1:
                return 0
            pop = x % 10
            if x < 0 and pop > 0:
                pop -= 10  # python负数取余问题

            x = (x - pop) // 10
            res = res * 10 + pop
        return res

# @lc code=end

