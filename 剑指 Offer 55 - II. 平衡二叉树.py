class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 自底向上 DFS
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return dfs(root) != -1