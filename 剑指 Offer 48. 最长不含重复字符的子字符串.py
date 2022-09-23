class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        # 1. 动态规划+哈希表 O(N) O(1)
        tmp = 0
        repeated = {}
        for j in range(n):
            left = repeated.get(s[j], -1)
            repeated[s[j]] = j
            if tmp < j - left:
                tmp += 1
            else:
                tmp = j - left
            res = max(res, tmp)
        return res

        # # 2. 双指针+哈希表 O(N) O(1)

        # # 2.1
        # repeated = set()
        # right = -1
        # for i in range(n):
        #     if i:
        #         repeated.remove(s[i-1])
        #     while right+1 < n and s[right+1] not in repeated:
        #         repeated.add(s[right+1])
        #         right += 1
        #     res = max(res, right-i+1)
        # return res

        # # 2.2
        # repeated = {}
        # left = -1

        # for i in range(n):
        #     if s[i] in repeated:
        #         left = max(repeated[s[i]], left)
        #     repeated[s[i]] = i
        #     res = max(res, i-left)
        
        # return res