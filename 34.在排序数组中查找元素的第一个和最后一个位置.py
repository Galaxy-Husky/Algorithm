#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (38.94%)
# Likes:    324
# Dislikes: 0
# Total Accepted:    65.2K
# Total Submissions: 166.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1. 二分查找 查找左右边界 O(logN) O(1)
        def binarysearch_left(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid - 1
            leftborder = right
            return leftborder

        def binarysearch_right(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            rightborder = left
            return rightborder

        # # 1.1 [左边界+1, 右边界-1]
        leftborder, rightborder = binarysearch_left(target), binarysearch_right(target)
        if leftborder+1 > rightborder-1:
            return [-1, -1]
        return [leftborder+1, rightborder-1]

        # 1.2 [左边界+1, (target+1)左边界]
        leftborder, leftborder2 = binarysearch_left(target), binarysearch_left(target+1)
        if leftborder+1 > leftborder2:
            return [-1, -1]
        return [leftborder+1, leftborder2]
# @lc code=end
