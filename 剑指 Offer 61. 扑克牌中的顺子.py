class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # 非排序
        min_val, max_val = 14, 1
        s = set()
        for n in nums:
            if n == 0:
                continue
            if n in s:
                return False
            s.add(n)
            min_val = min(min_val, n)
            max_val = max(max_val, n)
        return max_val - min_val + 1 <= 5
        """ # 排序
        nums.sort()
        zero = 0
        for i in range(4):
            if nums[i] == 0:
                zero += 1
                continue
            if nums[i] == nums[i+1]:
                return False
            zero -= nums[i+1] - nums[i] -1
        return zero >= 0 """