#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# https://leetcode.cn/problems/reverse-string/description/
#
# algorithms
# Easy (79.05%)
# Likes:    652
# Dislikes: 0
# Total Accepted:    604.2K
# Total Submissions: 764.2K
# Testcase Example:  '["h","e","l","l","o"]'
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
# 
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = ["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = ["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s[i] 都是 ASCII 码表中的可打印字符
# 
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        # """

        # # 1. python reverse
        # s.reverse()

        # 2. 双指针
        # 2.1
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # # 2.2
        # for i in range(len(s)//2):
        #     s[i], s[-i-1] = s[-i-1], s[i]

        # # 3. ([::-1]错误，切片生成新列表)
        # s[:] = s[::-1]
# @lc code=end

