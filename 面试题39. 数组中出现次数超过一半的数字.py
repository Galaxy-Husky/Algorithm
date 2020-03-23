class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ # 哈希表
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > len(nums) // 2:
                return i """
        """ # 排序
        nums.sort()
        return nums[len(nums) // 2] """
        # Boyer-Moore 投票
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate