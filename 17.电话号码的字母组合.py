#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.79%)
# Likes:    2128
# Dislikes: 0
# Total Accepted:    578.7K
# Total Submissions: 1M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # # 1. 递归 O(3^m*4^n) O(m+n)

        # # 1.1
        # # def backtrack(index):
        # #     if index == len(digits):
        # #         res.append(''.join(comb))
        # #     else:
        # #         digit = digits[index]
        # #         for letter in phone_map[digit]:
        # #             comb.append(letter)
        # #             backtrack(index+1)
        # #             comb.pop()

        # # comb = []
        # # res = []
        # # backtrack(0)
        # # return res

        # # 1.2
        # def backtrack(comb, nextdigits):
        #     if len(nextdigits) == 0:
        #         res.append(comb)
        #     else:
        #         for letter in phone_map[nextdigits[0]]:
        #             backtrack(comb+letter, nextdigits[1:])

        # res = []
        # backtrack('', digits)
        # return res

        # 2. 迭代 队列 O(3^m*4^n) O(m+n)
        q = ['']
        for digit in digits:
            for _ in range(len(q)):
                tmp = q.pop(0)
                for letter in phone_map[digit]:
                    q.append(tmp+letter)
        return q

# @lc code=end

