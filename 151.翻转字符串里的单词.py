#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (36.73%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    36.1K
# Total Submissions: 97.9K
# Testcase Example:  '"the sky is blue"'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 
# 
# 示例 1：
# 
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 
# 
# 示例 2：
# 
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 
# 
# 示例 3：
# 
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 说明：
# 
# 
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 
# 
# 
# 
# 进阶：
# 
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        """ #分词 反转 拼接
        return ' '.join(reversed(s.split())) """
        # 反转字符串 反转单词 去除空格
        def reverse_sentence(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr

        def reverse_word(arr):
            i = j = 0
            n = len(arr)
            while i < n:
                while i < n and arr[i] == ' ':
                    i += 1
                j = i
                while j < n and arr[j] != ' ':
                    j += 1
                reverse_sentence(arr, i, j-1)
                i = j
            return arr

        def trim_spaces(arr):
            n = len(arr)
            i, j = 0, n-1
            while i < j and arr[i] == ' ':
                i += 1
            while i < j and arr[j] == ' ':
                j -= 1
            return arr[i:j+1]
        
        def remove_spaces(arr):
            if ''.join(arr) == ' ':
                return []
            res = [arr[0]]
            for i in range(1, len(arr)):
                if arr[i] == ' ' and res[-1] == ' ':
                    continue
                res.append(arr[i])
            return res

        if not s:
            return ''
        arr = list(s)
        arr = reverse_sentence(arr, 0, len(arr)-1)
        arr = reverse_word(arr)
        arr = trim_spaces(arr)
        res = remove_spaces(arr)
        return ''.join(res)

# @lc code=end

