#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode.cn/problems/edit-distance/description/
#
# algorithms
# Hard (62.72%)
# Likes:    2648
# Dislikes: 0
# Total Accepted:    312.6K
# Total Submissions: 498.2K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. 动态规划

        # 1.1 O(MN) O(MN)
        n1, n2 = len(word1), len(word2)
        # dp = [[0] * (n2+1) for _ in range(n1+1)]

        # for i in range(n1+1):
        #     for j in range(n2+1):
        #         if i == 0:
        #             dp[i][j] = j
        #         elif j == 0:
        #             dp[i][j] = i
        #         else:
        #             if word1[i-1] == word2[j-1]:
        #                 dp[i][j] = dp[i-1][j-1]
        #             else:
        #                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # return dp[-1][-1]

        # 1.2 优化 O(MN) O(N)
        dp = [0] * (n2 + 1)
        prev = 0
        for i in range(n1+1):
            for j in range(n2+1):
                tmp = dp[j]
                if i == 0:
                    dp[j] = j
                elif j == 0:
                    dp[j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[j] = prev
                    else:
                        dp[j] = min(dp[j], prev, dp[j-1]) + 1
                prev = tmp
        return dp[-1]
                
# @lc code=end

