class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        '''# 快慢双指针
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] %2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums'''

        # 首尾双指针
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] %2 == 1:
                left += 1
            while left < right and nums[right] %2 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
