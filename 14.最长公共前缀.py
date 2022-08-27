#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (42.87%)
# Likes:    2411
# Dislikes: 0
# Total Accepted:    918.3K
# Total Submissions: 2.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    #     # 1. 横向扫描
    #     prefix = strs[0]
    #     count = len(strs)
    #     for i in range(1, count):
    #         prefix = self.lcp(prefix, strs[i])
    #         if not prefix:
    #             break
    #     return prefix

    # def lcp(self, str1, str2):
    #     length = min(len(str1), len(str2))
    #     index = 0
    #     while index < length and str1[index] == str2[index]:
    #         index +=1
    #     return str1[:index]

        # 2. 纵向扫描
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            char = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]

        # # 3. python max min
        # min_str = min(strs)
        # max_str = max(strs)
        # for i, c in enumerate(min_str):
        #     if c != max_str[i]:
        #         return max_str[:i]
        # return min_str

        # # 4. python lsit(zip*)
        # ss = list(map(set, zip(*strs)))
        # res = ""
        # for i, c in enumerate(ss):
        #     if len(c) > 1:
        #         break
        #     res += list(c)[0]
        # return res
# @lc code=end

