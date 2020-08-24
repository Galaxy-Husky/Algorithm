#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (37.14%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 27.1K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 示例:
# 
# 输入: 13
# 输出: 6 
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        high, digit, low, res = n, 1, 0, 0
        while high > 0:
            cur = high % 10
            high //= 10
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit 
            digit *= 10
        return res

# @lc code=end

