class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 字符串排序规则+快排
        def partition(strs, start, end):
            pivot = strs[start]
            low, high = start, end
            while low < high:
                while low < high and strs[high] + pivot >= pivot + strs[high]:
                    high -= 1
                while low < high and strs[low] + pivot <= pivot + strs[low]:
                    low += 1
                strs[high], strs[low] = strs[low], strs[high]
            strs[low], strs[start] = strs[start], strs[low]
            return low

        def quick_sort(alist, start, end):
            if start >= end:
                return
            pivot_index = partition(alist, start, end)
            quick_sort(alist, start, pivot_index - 1)
            quick_sort(alist, pivot_index + 1, end)

        strs = [str(num) for num in nums]
        quick_sort(strs, 0, len(strs) - 1)
        return ''.join(strs)