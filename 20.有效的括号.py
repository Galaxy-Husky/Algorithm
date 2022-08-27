#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.82%)
# Likes:    1385
# Dislikes: 0
# Total Accepted:    203.8K
# Total Submissions: 499K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 栈：开入闭出

        # 1. 闭key开value
        # paren_dict = {')': '(', '}': '{', ']': '['}
        # stack = []
        # for p in s:
        #     if p not in paren_dict:
        #         stack.append(p)
        #     else:
        #         if not stack or paren_dict[p] != stack.pop():
        #             return False
        # return not stack

        # 2.开key闭value
        paren_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if p in paren_dict:
                stack.append(p)
            else:
                if not stack or paren_dict[stack.pop()] != p:
                    return False
        return not stack

        # # python replace
        # while len(s) > 0:
        #     length = len(s)
        #     s = s.replace('()', '').replace('{}', '').replace('[]', '')
        #     if length == len(s):
        #         return False
        # return True


# @lc code=end

