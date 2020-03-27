#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (54.06%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 46.2K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
# 
# 示例 1:
# 
# 输入: a = 1, b = 2
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: a = -2, b = 3
# 输出: 1
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        while b:
            tmp = a ^ b
            b = (a & b) << 1 & mask
            a = tmp
        return a if a < 0x80000000 else ~(a ^ mask)
        
# @lc code=end

