class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 哈希表
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)

        ''' # 排序
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i] '''
                
        '''# 原地交换
        i = 0 
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]'''
        