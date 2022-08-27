#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode.cn/problems/contains-duplicate/description/
#
# algorithms
# Easy (55.74%)
# Likes:    802
# Dislikes: 0
# Total Accepted:    642.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1]'
#
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：false
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # 1. 数组和集合元素个数不同
        # return len(nums) > len(set(nums))

        # # 2. 排序
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # 3. 哈希表
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = 1
        return False

# @lc code=end

