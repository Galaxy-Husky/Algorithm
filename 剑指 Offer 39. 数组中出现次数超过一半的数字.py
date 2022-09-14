class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # 1. 排序 O(nlogn) O(logn)
        # nums.sort()
        # return nums[len(nums) // 2]

        # 2. 哈希表 O(N) O(N)
        # # 2.1
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        #     if d[i] > len(nums) // 2:
        #         return i

        # # 2.2
        # counts = Counter(nums)
        # return max(counts.keys(), key=counts.get)


        # 3. Boyer-Moore 投票 O(N) O(1)
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate