#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.56%)
# Likes:    2889
# Dislikes: 0
# Total Accepted:    598.2K
# Total Submissions: 771.3K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. 递归 O(4^n/n*) O(N)

        # # 1.1 
        # res = []

        # def backtrack(s, left, right):
        #     if right == n:
        #         res.append(''.join(s))
        #         return
        #     if left < n:
        #         s.append('(')
        #         backtrack(s, left+1, right)
        #         s.pop()
        #     if right < left:
        #         s.append(')')
        #         backtrack(s, left, right+1)
        #         s.pop()
        
        # backtrack([], 0, 0)
        # return res

        # 1.2
        res = []

        def backtrack(s, left, right):
            if right == n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        
        backtrack('', 0, 0)
        return res
# @lc code=end

