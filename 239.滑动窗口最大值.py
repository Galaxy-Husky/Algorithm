#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (43.70%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    28.5K
# Total Submissions: 65.2K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 示例:
# 
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 
# 提示：
# 
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
# 
# 
# 
# 进阶：
# 
# 你能在线性时间复杂度内解决此题吗？
# 
#

# @lc code=start
import heapq
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 1. 大根堆 O(NlogN) O(N)
        # heap = [(-nums[i], i) for i in range(k)]
        # heapq.heapify(heap)
        # res = [-heap[0][0]]
        # for i in range(k, len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     while heap[0][1] <= i - k:
        #         heapq.heappop(heap)
        #     res.append(-heap[0][0])
        # return res

        # 2. 单调队列+存储下标 O(N) O(k)
        deq = collections.deque()
        for i in range(k):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        
        res = [nums[deq[0]]]
        for i in range(k, len(nums)):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if deq[0] <= i - k:
                deq.popleft()
            res.append(nums[deq[0]])
        return res
        
# @lc code=end

