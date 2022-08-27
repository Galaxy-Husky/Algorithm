#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (62.73%)
# Likes:    524
# Dislikes: 0
# Total Accepted:    146.6K
# Total Submissions: 233.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # 1. 排序
        # nums.sort()
        # return nums[len(nums) // 2]

        # 2. 哈希表
        # # 2.1
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        #     if d[i] > len(nums) // 2:
        #         return i

        # # 2.2
        # counts = Counter(nums)
        # return max(counts.keys(), key=counts.get)


        # 3. Boyer-Moore 投票
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate

# @lc code=end

