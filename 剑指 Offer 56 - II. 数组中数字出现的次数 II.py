class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ # HashSet + 求和
        return (3 * sum(set(nums)) - sum(nums)) // 2 """
        # HashMap
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for key, value in dic.items():
            if value == 1:
                return key