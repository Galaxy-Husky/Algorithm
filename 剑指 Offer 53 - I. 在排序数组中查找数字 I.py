class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        # 查找边界 right-left-1
        '''# 查找右边界
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1
        right = i

        # 查找左边界
        i = 0
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        left = i

        return right - left - 1'''

        # target右边界- (target-1)右边界
        '''def helper(target):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return i

        return helper(target) - helper(target - 1)'''
