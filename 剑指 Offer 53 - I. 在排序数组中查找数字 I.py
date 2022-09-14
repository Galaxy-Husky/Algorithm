class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找 查找左边界 O(logn) O(1)
        def binarysearch(target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid
            return left

        leftborder, rightborder = binarysearch(target), binarysearch(target+1)
        return rightborder-leftborder
