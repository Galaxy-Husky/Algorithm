class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ''' # 排序
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i] '''
        # 哈希表
        d = {}
        for n in (nums):
            if n in d:
                return n
            else:
                d[n] = 0