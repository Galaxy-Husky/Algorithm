class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口-双指针 O(target) O(1)
        left, right, s = 1, 2, 3
        res = []
        while left < right:
            if s == target:
                res.append(list(range(left, right+1)))
            if s < target:
                right += 1
                s += right
            else:
                s -= left
                left += 1
        return res