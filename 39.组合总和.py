#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.36%)
# Likes:    554
# Dislikes: 0
# Total Accepted:    72.5K
# Total Submissions: 105.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS 回溯
        def dfs(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if target-candidates[i] < 0:
                    break
                dfs(i, target-candidates[i], path+[candidates[i]])
        candidates.sort()
        res = []
        dfs(0, target, [])
        return res
# @lc code=end

