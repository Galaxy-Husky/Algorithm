#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode.cn/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (79.07%)
# Likes:    1094
# Dislikes: 0
# Total Accepted:    335K
# Total Submissions: 423.7K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给你两棵二叉树： root1 和 root2 。
# 
# 
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为
# null 的节点将直接作为新二叉树的节点。
# 
# 返回合并后的二叉树。
# 
# 注意: 合并过程必须从两个树的根节点开始。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# 输出：[3,4,5,5,4,null,7]
# 
# 
# 示例 2：
# 
# 
# 输入：root1 = [1], root2 = [1,2]
# 输出：[2,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 两棵树中的节点数目在范围 [0, 2000] 内
# -10^4 <= Node.val <= 10^4
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
from collections import deque


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # # 1. 递归 O(min(m,n)) O(min(m,n))
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # merged = TreeNode(root1.val+root2.val)
        # merged.left = self.mergeTrees(root1.left, root2.left)
        # merged.right = self.mergeTrees(root1.right, root2.right)
        # return merged

        # 2. 迭代 O(min(m,n)) O(min(m,n))
        if not (root1 and root2):
            return root1 or root2
        q1, q2 = deque([root1]), deque([root2])
        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1 and node2:
                node1.val += node2 .val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return root1
        
# @lc code=end

