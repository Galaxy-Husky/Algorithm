class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. 二分查找 查找左右边界 O(logN) O(1)
        def binarysearch_left(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid - 1
            leftborder = right
            return leftborder

        def binarysearch_right(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            rightborder = left
            return rightborder

        # # 1.1 右边界-左边界-1
        # leftborder, rightborder = binarysearch_left(target), binarysearch_right(target)
        # return rightborder - leftborder - 1

        # 1.2 (target+1)左边界-左边界
        leftborder, leftborder2 = binarysearch_left(target), binarysearch_left(target+1)
        return leftborder2 - leftborder
