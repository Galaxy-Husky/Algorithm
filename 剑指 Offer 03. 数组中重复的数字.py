class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # # 1. 哈希表 O(N) O(N)
        # s = set()
        # for n in nums:
        #     if n in s:
        #         return n
        #     else:
        #         s.add(n)
                
        # 2. 原地交换 O(N) O(1)
        i = 0 
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        # # 3. 排序
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        