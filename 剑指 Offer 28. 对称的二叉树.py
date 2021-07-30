# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ # 递归
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        return recur(root.left, root.right) if root else True """

        # 迭代-队列
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
            q += [l.left, r.right, l.right, r.left]
        return True