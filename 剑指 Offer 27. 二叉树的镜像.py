class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # DFS 递归
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root