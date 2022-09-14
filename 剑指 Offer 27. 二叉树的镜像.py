# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # # 1. 递归 O(N) O(N)
        # if not root:
        #     return None
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # 2. 栈 O(N) O(N)
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root