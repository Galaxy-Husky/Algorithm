#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#
# https://leetcode.cn/problems/nth-digit/description/
#
# algorithms
# Medium (45.62%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 115.2K
# Testcase Example:  '3'
#
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n
# 位上的数字。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1. 找规律 O(log10^N) O(logN)
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit 
        return int(str(num)[(n - 1) % digit])
# @lc code=end

