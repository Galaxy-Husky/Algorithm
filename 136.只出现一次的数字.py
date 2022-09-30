#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (69.65%)
# Likes:    1446
# Dislikes: 0
# Total Accepted:    257.7K
# Total Submissions: 370.1K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#

# @lc code=start
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 额外空间 O(N) O(N)
        # 1. 集合：没有加入，已有删除
        # 2. 集合：数组之和-集合之和
        # 3. 哈希表：{数字：次数}

        # 额外时间 O(NlogN) O(1)
        # 1. 排序：相邻元素重复

        # 1. 位运算-异或 O(N) O(1)
        res = 0
        for n in nums:
            res ^= n
        return res

        # # 2. reduce
        # return reduce(lambda x, y: x ^ y, nums)
# @lc code=end

