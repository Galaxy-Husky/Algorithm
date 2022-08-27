#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (74.19%)
# Likes:    473
# Dislikes: 0
# Total Accepted:    262.7K
# Total Submissions: 354K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 示例 2:
# 
# 
# 输入： s = "God Ding"
# 输出："doG gniD"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^4
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # # 1. 切片 遍历反转 连接
        # return " ".join(word[::-1] for word in s.split())

        # 2. 两次反转
        return  " ".join(s.split()[::-1])[::-1]

        # # 3. 双指针 (python 不可原地修改str)
        # i = 0
        # length = len(s)
        # while i < length:
        #     start = i
        #     while i < length and s[i] != ' ':
        #         i += 1
        #     left, right = start, i - 1
        #     while left < right:
        #         s[left], s[right] = s[right], s[left]
        #         left += 1
        #         right -= 1
        #     while i < length and s[i] == ' ':
        #         i += 1
        # return s

# @lc code=end

