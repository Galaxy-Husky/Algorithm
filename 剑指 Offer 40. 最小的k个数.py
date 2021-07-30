import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """ # 排序
        arr.sort()
        return arr[:k] """

        '''# 快排
        def quicksort(arr, left, right):
            if left >= right:
                return
            i, j = left, right
            while i < j:
                while i < j and arr[j] >= arr[left]:
                    j -= 1
                while i < j and arr[i] <= arr[left]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[left] = arr[left], arr[i]
            quicksort(arr, left, i - 1)
            quicksort(arr, i + 1, right)

        quicksort(arr, 0, len(arr) - 1)
        return arr[:k]'''

        # 快速选择
        def quicksort(arr, left, right):
            if left >= right:
                return arr[:k]
            i, j = left, right
            while i < j:
                while i < j and arr[j] >= arr[left]:
                    j -= 1
                while i < j and arr[i] <= arr[left]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[left] = arr[left], arr[i]
            if k < i:
                return quicksort(arr, left, i - 1)
            elif k > i:
                return quicksort(arr, i + 1, right)
            else:
                return arr[:k]

        return quicksort(arr, 0, len(arr) - 1)

        '''# 最大堆
        if k == 0:
            return []
        max_heap = [-x for x in arr[:k]]
        heapq.heapify(max_heap)
        for i in range(k, len(arr)):
            if -arr[i] > max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -arr[i])
        return [-x for x in max_heap]'''
