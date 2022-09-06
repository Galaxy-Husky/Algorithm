#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode.cn/problems/3sum-closest/description/
#
# algorithms
# Medium (45.58%)
# Likes:    1223
# Dislikes: 0
# Total Accepted:    397.1K
# Total Submissions: 871.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 
# 返回这三个数的和。
# 
# 假定每组输入只存在恰好一个解。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序 + 双指针
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return s
                if s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < target:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

# @lc code=end

