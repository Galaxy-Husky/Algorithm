from bisect import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 1. 归并排序 O(NlogN) O(N)

        def merge_sort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            left_count = merge_sort(left, mid)
            right_count = merge_sort(mid+1, right)
            return left_count + right_count + merge(left, mid, right)

        def merge(left, mid, right):
            i, j = left, mid + 1
            cross_count = 0
            sorted_list = []
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    sorted_list.append(nums[i])
                    i += 1
                else:
                    cross_count += mid - i + 1
                    sorted_list.append(nums[j])
                    j += 1
            if i <= mid:
                sorted_list.extend(nums[i:mid+1])
            if j <= right:
                sorted_list.extend(nums[j:right+1])
            nums[left:right+1] = sorted_list
            return cross_count
        
        return merge_sort(0, len(nums)-1)

        # # 2. 二分查找+有序插入 O(NlogN*切片插入) O(1)
        # q = []
        # count = 0
        # for n in nums:
        #     i = bisect.bisect_left(q, -n)
        #     count += i
        #     q[i:i] = [-n]
        # return count



