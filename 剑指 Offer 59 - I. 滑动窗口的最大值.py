from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列 -> 单调队列
        deq, res = deque(), []
        for i in range(len(nums)):
            if deq and i - deq[0] == k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res