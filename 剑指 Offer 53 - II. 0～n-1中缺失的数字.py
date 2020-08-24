class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left