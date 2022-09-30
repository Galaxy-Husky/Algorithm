#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode.cn/problems/counting-bits/description/
#
# algorithms
# Easy (78.69%)
# Likes:    1094
# Dislikes: 0
# Total Accepted:    250.5K
# Total Submissions: 318.3K
# Testcase Example:  '2'
#
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans
# 作为答案。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# 
# 进阶：
# 
# 
# 很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
# 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # # 1. 位运算 O(NlogN) O(1)
        # def count_ones(x):
        #     count = 0
        #     while x:
        #         x &= x - 1
        #         count += 1
        #     return count
        # return [count_ones(i) for i in range(n+1)]

        # 2. 动态规划 O(N) O(1)
        # 2.1
        count = [0]*(n+1)
        for i in range(1, n+1):
            if i % 2:
                count[i] = count[i-1] + 1
            else:
                count[i] = count[i//2]
        return count

        # # 2.2
        # count = [0]
        # for i in range(1, n+1):
        #     count.append(count[i//2]+(i & 1))
        # return count

        # # 2.3
        # count = [0]
        # for i in range(1, n+1):
        #     count.append(count[i&(i-1)] + 1)
        # return count

# @lc code=end

