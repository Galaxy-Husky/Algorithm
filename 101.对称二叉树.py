#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.50%)
# Likes:    668
# Dislikes: 0
# Total Accepted:    110.7K
# Total Submissions: 219.1K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    def isSymmetric(self, root: TreeNode) -> bool:
        # # 1. 递归 O(N) O(N)
        # def recur(L, R):
        #     if not L and not R:
        #         return True
        #     if not L or not R or L.val != R.val:
        #         return False
        #     return recur(L.left, R.right) and recur(L.right, R.left)
        # return recur(root.left, root.right) if root else True

        # 2. 迭代 队列 O(N) O(N)
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            l = q.pop(0)
            r = q.pop(0)
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            q.extend([l.left, r.right, l.right, r.left])
        return True
        
# @lc code=end

