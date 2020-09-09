#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.62%)
# Likes:    2647
# Dislikes: 0
# Total Accepted:    367K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划 + 竖着填表
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        start, max_l = 0, 0
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1] 
                if dp[i][j]:
                    cur_l = j - i + 1
                    if  cur_l > max_l:
                        max_l = cur_l
                        start = i
        return s[start:start+max_l]
# @lc code=end

