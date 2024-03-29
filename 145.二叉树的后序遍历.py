#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (70.07%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 74.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     # 1. 递归 O(N) O(N)
    #     def postorder(root):
    #         if not root:
    #             return
    #         postorder(root.left)
    #         postorder(root.right)
    #         res.append(root.val)
        
    #     res = []
    #     postorder(root)
    #     return res

        # 2. 迭代 前序遍历逆序 O(N) O(N)
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]
# @lc code=end

