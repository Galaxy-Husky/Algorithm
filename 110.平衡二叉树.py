#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (50.83%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 118.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 1. 递归

        # # 1.1  自顶向下 O(nlogn) O(n)
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left), dfs(root.right)) + 1

        # if not root:
        #     return True
        # return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        # 1.2 自底向上 O(n) O(n)
        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            if left_height == -1:
                return -1
            right_height = dfs(root.right)
            if right_height == -1:
                return -1
            return max(left_height, right_height) + 1 if abs(left_height - right_height) <= 1 else -1
        return dfs(root) != -1
# @lc code=endmn

