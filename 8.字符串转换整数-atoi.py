#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (19.07%)
# Likes:    574
# Dislikes: 0
# Total Accepted:    117K
# Total Submissions: 608.2K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 
# 
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 
# 说明：
# 
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX
# (2^31 − 1) 或 INT_MIN (−2^31) 。
# 
# 示例 1:
# 
# 输入: "42"
# 输出: 42
# 
# 
# 示例 2:
# 
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 
# 
# 示例 3:
# 
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 
# 
# 示例 4:
# 
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
# 
# 示例 5:
# 
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
# 因此返回 INT_MIN (−2^31) 。
# 
# 
#

# @lc code=start
import re

min_value, max_value = -2**31, 2**31-1

class Automation:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_num', 'end'],
            'signed': ['end', 'end', 'in_num', 'end'],
            'in_num': ['end', 'end', 'in_num', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_index(self, c):
        if c.isspace():
            return 0
        if c in '+-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_index(c)]
        if self.state == 'in_num':
            self.ans = self.ans*10 + int(c)
            self.ans = min(self.ans, max_value) if self.sign == 1 else min(self.ans, -min_value)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:

        # # 1. 正则
        # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), max_value), min_value)

        # 2. 去除空格0->判断正负->ord转换数字->判断溢出 O(N) O(1)
        if not s:
            return 0
        i = 0
        while s[i] == ' ':
            i += 1
            if i == len(s):
                return 0
        base = 0
        sign = -1 if s[i] == '-' else 1
        if s[i] in '+-':
            i += 1
        for c in s[i:]:
            if not '0' <= c <= '9':
                break
            digit = ord(c) - ord('0')
            if base > max_value // 10 or base == max_value // 10 and digit > max_value % 10:
                return max_value if sign == 1 else min_value
            base = 10 * base + digit
        return base * sign

        # # 3. DFA O(N) O(1)
        # auto = Automation()
        # for c in s:
        #     auto.get(c)
        # return auto.sign * auto.ans
# @lc code=end

