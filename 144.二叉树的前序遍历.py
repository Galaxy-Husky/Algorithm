#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (64.01%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    70.7K
# Total Submissions: 109.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # 1. 递归 O(N) O(N)
        # def preorder(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # res = []
        # preorder(root)
        # return res

        # 2. 迭代 O(N) O(N)
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
# @lc code=end

