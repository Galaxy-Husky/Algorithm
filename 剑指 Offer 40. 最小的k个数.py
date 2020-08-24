import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """ # 排序
        arr.sort()
        return arr[:k] """
        # 最大堆
        if k == 0:
            return []
        hq = [-x for x in arr[:k]]
        heapq.heapify(hq)
        for i in range(k, len(arr)):
            if arr[i] < -hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, -arr[i])
        res = [-x for x in hq]
        return res

