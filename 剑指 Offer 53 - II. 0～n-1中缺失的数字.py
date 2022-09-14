class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # 1. 排序 O(n) O(1)
        # for i, num in enumerate(nums):
        #     if num != i:
        #         return i
        # return len(nums)

        # # 2. 哈希表 O(n) O(n)
        # s = set(nums)
        # for i in range(len(nums) + 1):
        #     if i not in s:
        #         return i

        # # 3. 位运算 异或 O(n) O(1)
        # xor = 0
        # for i, num in enumerate(nums):
        #     xor ^= i ^ num
        # return xor ^ len(nums)

        # 3. 二分查找 O(logn) O(1) 
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left