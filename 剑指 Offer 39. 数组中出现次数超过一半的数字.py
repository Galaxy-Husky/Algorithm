class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''# 哈希表
        counter = collections.Counter(nums)
        return max(counter.keys(), key=counter.get)

        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > len(nums) // 2:
                return i'''

        """ # 排序
        nums.sort()
        return nums[len(nums) // 2] """

        # Boyer-Moore 投票
        votes, candidate = 0, None
        for num in nums:
            if votes == 0:
                candidate = num
            votes += 1 if candidate == num else -1
        return candidate