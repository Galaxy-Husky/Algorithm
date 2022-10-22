#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (70.16%)
# Likes:    1136
# Dislikes: 0
# Total Accepted:    222.2K
# Total Submissions: 316.7K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
# 
# 
# 
# 示例 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# inorder.length == preorder.length
# -3000 
# preorder 和 inorder 均无重复元素
# inorder 均出现在 preorder
# preorder 保证为二叉树的前序遍历序列
# inorder 保证为二叉树的中序遍历序列
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 1. 递归 O(N) O(N)
        if inorder:
            ind = inorder.index(preorder[0])
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder[1:ind+1], inorder[0:ind])
            root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
            return root

# @lc code=end

