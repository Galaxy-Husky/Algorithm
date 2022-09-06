#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (61.03%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    81.7K
# Total Submissions: 133.5K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # 1. 堆排序
        
        # # 1.1 heapq （小根堆）
        # # 1.1.1 
        # return heapq.nlargest(k, nums)[-1]

        # # 1.1.2
        # min_heap = []
        # for i in range(k):
        #     heapq.heappush(min_heap, nums[i])
        # for j in range(k, len(nums)):
        #     min_value = min_heap[0]
        #     if nums[j] > min_value:
        #         heapq.heapreplace(min_heap, nums[j])
        # return min_heap[0]

        # # 1.2 heapq （大根堆）
        # max_heap = [-x for x in nums]
        # heapq.heapify(max_heap)
        # for _ in range(k-1):
        #     heapq.heappop(max_heap)
        # return -max_heap[0]

        # 2. 快速排序->快速选择
        return self.quickselect(nums, 0, len(nums)-1, len(nums) - k)

    def quickselect(self, nums, left, right, target):

        def partition(nums, left, right):
            pivot_index = left
            pivot = nums[pivot_index]
            low, high = left + 1, right
            while True:
                while low <= high and nums[low] < pivot:
                    low += 1
                while high >= low and nums[high] >= pivot:
                    high -= 1
                if low > high:
                    break
                else:
                    nums[low], nums[high] = nums[high], nums[low]
            nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
            return high
            
        pivot_index = partition(nums, left, right)
        if pivot_index == target:
            return nums[pivot_index]
        elif pivot_index < target:
            return self.quickselect(nums, pivot_index+1, right, target)
        else:
            return self.quickselect(nums, left, pivot_index-1, target)
                


# @lc code=end

