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
        """ # DFS 递归
        if not root:
            return True
        def mirror(t1, t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            else:
                return mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
        return mirror(root.left, root.right) """
        # BFS 迭代 队列
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            l = q.pop(0)
            r = q.pop(0)
            if l == None and r == None:
                continue
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            q += [l.left, r.right, l.right, r.left]
        return True
        
# @lc code=end

