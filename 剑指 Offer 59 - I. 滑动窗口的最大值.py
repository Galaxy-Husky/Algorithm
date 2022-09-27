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