#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (46.57%)
# Likes:    414
# Dislikes: 0
# Total Accepted:    107.9K
# Total Submissions: 231.7K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 直接合并排序
        # nums1[m:] = nums2
        # nums1.sort()

        # 双指针
        # # 1.从前往后
        # sorted = []
        # p1 = p2 = 0
        # while p1 < m or p2 < n:
        #     if p1 == m:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        #     elif p2 == n:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        # nums1[:] = sorted

        # 2. 从后往前
        # 2.1 
        # p1 = m - 1
        # p2 = n - 1
        # p = m + n -1
        # while p1 >= 0 or p2 >= 0:
        #     if p1 == -1:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     elif p2 == -1:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     elif nums1[p1] < nums2[p2]:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     else:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     p -= 1
        
        # 2.2
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        nums1[:n] = nums2[:n]         
        
# @lc code=end

