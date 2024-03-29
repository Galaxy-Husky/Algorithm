class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 除大小王无重复 max - min < 5
        
        # # 1. 集合+遍历 O(N)=O(1) O(N)=O(1)
        # min_val, max_val = 14, 0
        # s = set()
        # for n in nums:
        #     if n == 0:
        #         continue
        #     if n in s:
        #         return False
        #     s.add(n)
        #     min_val = min(min_val, n)
        #     max_val = max(max_val, n)
        # return max_val - min_val < 5

        # 2. 排序+遍历 O(NlogN)=O(1) O(N)=O(1)
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
                continue
            if nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5
