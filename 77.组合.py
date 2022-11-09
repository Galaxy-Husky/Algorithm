#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
#  
#
# algorithms
# Medium (72.66%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 52.8K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """ """ # DFS 回溯
        def dfs(start, k, path):
            if k == 0:
                res.append(path)
                return 
            for i in range(start, n+1):
                dfs(i+1, k-1, path+[i])

        res = []
        dfs(1, k, []) 
        return res
        """ # DFS 回溯
        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(i+1, path)
                path.pop()
        res = []
        dfs(1, [])
        return res """
# @lc code=end

