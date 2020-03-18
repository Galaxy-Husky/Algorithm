#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (53.57%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 14.5K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
# 
# 示例:
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 说明:
# 
# 
# 数组仅可以在 update 函数下进行修改。
# 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
# 
# 
#

# @lc code=start
""" class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left_node = None
        self.right_node = None

class NumArray:
    # 线段树：结点+递归
    def __init__(self, nums: List[int]):
        def build(nums, l, r):
            if l > r:  # 空数组[]
                return None
            if l == r:
                n = TreeNode(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = TreeNode(l, r)
            root.left_node = build(nums, l, mid)
            root.right_node = build(nums, mid+1, r)
            root.total = root.left_node.total + root.right_node.total
            return root
        self.root = build(nums, 0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        def update_tree(root, i, val):
            if root.start == root.end:
                root.total = val
                return
            mid = (root.start + root.end) // 2
            if i <= mid:
                update_tree(root.left_node, i, val)
            else:
                update_tree(root.right_node, i, val)
            root.total = root.left_node.total + root.right_node.total
        update_tree(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def sum_tree(root, i, j):
            if i == root.start and j == root.end:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return sum_tree(root.left_node, i, j)
            if i > mid:
                return sum_tree(root.right_node, i, j)
            return sum_tree(root.left_node, i, mid) + sum_tree(root.right_node, mid+1, j)
        return sum_tree(self.root, i, j)  """

class NumArray:
    # 线段树：数组+递归
    def __init__(self, nums: List[int]):
        def build(nums, pos, start, end):
            if start > end:
                return
            if start == end:
                self.arr[pos] = nums[start]
                return
            mid = (start + end) // 2
            build(nums, 2*pos+1, start, mid)
            build(nums, 2*pos+2, mid+1, end)
            self.arr[pos] = self.arr[2*pos+1] + self.arr[2*pos+2]
        self.arr = [0] * len(nums) * 4
        self.len = len(nums) - 1
        build(nums, 0, 0, self.len)

    def update(self, i: int, val: int) -> None:
        def update_tree(pos, start, end, i, val):
            if start == end:
                self.arr[pos] = val
                return
            mid = (start + end) // 2
            if i <= mid:
                update_tree(2*pos+1, start, mid, i, val)
            else:
                update_tree(2*pos+2, mid+1, end, i, val)
            self.arr[pos] = self.arr[2*pos+1] + self.arr[2*pos+2]
        update_tree(0, 0, self.len, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def sum_tree(pos, start, end, i, j):
            if j < start or i > end:
                return 0
            if i <= start and j >= end:
                return self.arr[pos]
            mid = (start + end) // 2
            return sum_tree(2*pos+1, start, mid, i, j) + sum_tree(2*pos+2, mid+1, end, i, j)
        return sum_tree(0, 0, self.len, i, j) 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

