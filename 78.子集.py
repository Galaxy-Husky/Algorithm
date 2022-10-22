#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (76.36%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    68.9K
# Total Submissions: 89.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # 1. 二进制位 O(N*2^N) O(N)
        # n = len(nums)
        # res = []
        # for mask in range(0, 1 << n):
        #     tmp = []
        #     for i in range(n):
        #         if mask & (1 << i):
        #             tmp.append(nums[i])
        #     res.append(tmp)
        # return res

        # # 2. 迭代
        # res = [[]]
        # for num in nums:
        #     res.extend([[num] + item for item in res])
        # return res

        # 3. 回溯 O(N*2^N) O(N)
        res = []
        n = len(nums)

        # 3.1
        def dfs(start, path):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res

        # # 3.2
        # def dfs(start, path):
        #     res.append(path)
        #     for i in range(start, n):
        #         dfs(i+1, path+[nums[i]])
        # dfs(0, [])
        # return res


# @lc code=end

