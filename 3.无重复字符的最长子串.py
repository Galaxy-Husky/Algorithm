#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.01%)
# Likes:    8165
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 5.1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        # 1. 滑动窗口 双指针+哈希表 O(N) O(1)

        # # 1.1
        # repeated = set()
        # right = -1
        # for i in range(n):
        #     if i:
        #         repeated.remove(s[i-1])
        #     while right+1 < n and s[right+1] not in repeated:
        #         repeated.add(s[right+1])
        #         right += 1
        #     res = max(res, right-i+1)
        # return res

        # 1.2
        repeated = {}
        left = -1

        for i in range(n):
            if s[i] in repeated:
                left = max(repeated[s[i]], left)
            repeated[s[i]] = i
            res = max(res, i-left)
        
        return res

# @lc code=end

