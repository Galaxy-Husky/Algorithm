import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # # 1. 排序
        # arr.sort()
        # return arr[:k]

        # # 2. 最大堆 O(nlogk) O(k)
        # if k == 0:
        #     return []
        # max_heap = [-x for x in arr[:k]]
        # heapq.heapify(max_heap)
        # for i in range(k, len(arr)):
        #     if -arr[i] > max_heap[0]:
        #         heapq.heappop(max_heap)
        #         heapq.heappush(max_heap, -arr[i])
        # return [-x for x in max_heap]

        # # 2. 快排 O(nlogn) O(logN)
        # def quicksort(arr, left, right):

        #     def partition(arr, left, right):
        #         pivot_index = left
        #         pivot = arr[pivot_index]
        #         low, high = left+1, right
        #         while True:
        #             while low <= high and arr[high] >= pivot:
        #                 high -= 1
        #             while low <= high and arr[low] <= pivot:
        #                 low += 1
        #             if low > high:
        #                 break
        #             else:
        #                 arr[low], arr[high] = arr[high], arr[low]
        #         arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        #         return high
            
        #     if left > right:
        #         return
        #     pivot = partition(arr, left, right)
        #     quicksort(arr, left, pivot-1)
        #     quicksort(arr, pivot+1, right)
            
        # quicksort(arr, 0, len(arr) - 1)
        # return arr[:k]

        # 3. 快速选择 O(N) O(logn)
        def quickselect(arr, left, right):

            def partition(arr, left, right):
                pivot_index = left
                pivot = arr[pivot_index]
                low, high = left+1, right
                while True:
                    while low <= high and arr[high] >= pivot:
                        high -= 1
                    while low <= high and arr[low] <= pivot:
                        low += 1
                    if low > high:
                        break
                    else:
                        arr[low], arr[high] = arr[high], arr[low]
                arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
                return high
            
            pivot_index = partition(arr, left, right)

            if k < pivot_index:
                return quickselect(arr, left, pivot_index-1)
            elif k > pivot_index:
                return quickselect(arr, pivot_index+1, right)
            else:
                return arr[:k]

        if k >= len(arr):
            return arr
        return quickselect(arr, 0, len(arr) - 1)


