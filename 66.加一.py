#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (42.93%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    118.1K
# Total Submissions: 274.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. +1, 45 -> 46
        # 2. 进位, 499 -> 500
        # 3. 进位扩展, 999 -> 1000
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10 
            if digits[i] != 0:
                return digits
        digits.insert(0, 1)
        return digits
            
            
        
# @lc code=end

