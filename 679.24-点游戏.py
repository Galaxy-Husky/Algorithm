#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (54.87%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 34.5K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
# 
# 示例 1:
# 
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 1, 2]
# 输出: False
# 
# 
# 注意:
# 
# 
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
# 
# 
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # DFS 递归
        # 四个数取出两个数之后,做加减乘除处理之后加入到原数组中会剩下三个数,递归交给下一层去处理
        def dfs(nums):
            l = len(nums)
            if len(nums) == 1:
                return abs(nums[0] - 24) < eps
            for i in range(l):
                for j in range(i+1, l):
                    new_nums = [nums[k] for k in range(l) if i != k != j]
                    if dfs(new_nums+[nums[i] + nums[j]]) or dfs (new_nums+[nums[i] - nums[j]]) or dfs (new_nums+[nums[j] - nums[i]])\
                         or dfs(new_nums+[nums[i] * nums[j]]) or (abs(nums[j]) > eps and dfs(new_nums+[nums[i] / nums[j]]))\
                         or (abs(nums[i]) > eps and dfs(new_nums+[nums[j] / nums[i]])):
                        return True
            return False
        eps = 1e-6
        return dfs(nums)
# @lc code=end

