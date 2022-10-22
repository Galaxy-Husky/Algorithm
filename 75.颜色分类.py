#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode.cn/problems/sort-colors/description/
#
# algorithms
# Medium (60.09%)
# Likes:    1426
# Dislikes: 0
# Total Accepted:    457.4K
# Total Submissions: 760.9K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 
# 
# 
# 必须在不使用库的sort函数的情况下解决这个问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以不使用代码库中的排序函数来解决这道题吗？
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # # 1. 单指针 O(N) O(1)
        # ptr = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         nums[i], nums[ptr] = nums[ptr], nums[i]
        #         ptr += 1
        # for i in range(ptr, n):
        #     if nums[i] == 1:
        #         nums[i], nums[ptr] = nums[ptr], nums[i]
        #         ptr += 1
        
        # # 2. 双指针 O(N) O(1)

        # # 2.1 从左向右
        # p0 = p1 = 0
        # for i in range(n):
        #     if nums[i] == 1:
        #         nums[i], nums[p1] = nums[p1], nums[i]
        #         p1 += 1
        #     elif nums[i] == 0:
        #         nums[i], nums[p0] = nums[p0], nums[i]
        #         if p0 < p1:
        #             nums[i], nums[p1] = nums[p1], nums[i]
        #         p0 += 1
        #         p1 += 1

        # # 2.1 从右向左
        # p0, p2 = 0, n - 1
        # i = 0
        # while i <= p2:
        #     while i <= p2 and nums[i] == 2:
        #         nums[i], nums[p2] = nums[p2], nums[i]
        #         p2 -= 1
        #     if nums[i] == 0:
        #         nums[i], nums[p0] = nums[p0], nums[i]
        #         p0 += 1
        #     i += 1

        # 3. 三指针 O(N) O(1)
        p0, p1, p2 = 0, 0, n - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0] 
                p0 += 1
                p1 += 1
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

# @lc code=end

