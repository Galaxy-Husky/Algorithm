# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. 一次遍历

        #1.1 O(N) O(1)
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

        # # 1.2
        # if p.val > q.val:
        #     p, q = q, p
        # while root:
        #     if root.val < p.val:
        #         root = root.right
        #     elif root.val > q.val:
        #         root = root.left
        #     else:
        #         return root

        # # 2. 递归 O(N) O(N)
        # if (root.val - p.val) * (root.val - q.val) <= 0:
        #     return root
        # else:
        #     return self.lowestCommonAncestor(root.left if p.val < root.val else root.right, p, q)