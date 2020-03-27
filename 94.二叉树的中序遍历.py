#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (70.10%)
# Likes:    406
# Dislikes: 0
# Total Accepted:    108.5K
# Total Submissions: 154.4K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # DFS 栈 迭代
        res, stack = [], []
        cur = root
        while cur or stack:  # cur非空-> 还有左子树；stack非空->还有右子树
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res

# @lc code=end

