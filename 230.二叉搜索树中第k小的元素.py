#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (75.67%)
# Likes:    663
# Dislikes: 0
# Total Accepted:    233.3K
# Total Submissions: 308.2K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数为 n 。
# 1 
# 0 
# 
# 
# 
# 
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class mybst:
    def __init__(self, root):
        self.root = root
        self._nodenum = {}
        self._count_nodenum(root)
    
    def _count_nodenum(self, node):
        if not node:
            return 0
        self._nodenum[node] = 1 + self._count_nodenum(node.left) + self._count_nodenum(node.right)
        return self._nodenum[node]
    
    def _get_nodenum(self, node):
        return self._nodenum[node] if node else 0

    def kth_smallest(self, k):
        node = self.root
        while node:
            left = self._get_nodenum(node.left)
            if left < k-1:
                node = node.right
                k -= left+1
            elif left == k-1:
                return node.val
            else:
                node = node.left

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # 1. 中序遍历
        #  stack = []
        #  while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right

        # 2. 记录子树的结点数
        bst = mybst(root)
        return bst.kth_smallest(k)

# @lc code=end

