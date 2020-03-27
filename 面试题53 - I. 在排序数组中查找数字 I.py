class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if nums[left] != target:
            return 0
        first = left
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        last = left
        return last - first + 1