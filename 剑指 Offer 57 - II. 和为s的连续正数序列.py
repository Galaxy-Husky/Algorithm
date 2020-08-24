class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口
        left, right, res = 1, 2, []
        while left <= target // 2:
            alist = list(range(left, right+1))
            cur_sum = sum(alist)
            if cur_sum == target:
                res.append(alist)
                left += 2
            elif cur_sum < target:
                right += 1
            else:
                left += 1
        return res