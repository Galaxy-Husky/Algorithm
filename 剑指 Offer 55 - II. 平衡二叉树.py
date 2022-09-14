class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 1. 递归

        # # 1.1  自顶向下 O(nlogn) O(n)
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left), dfs(root.right)) + 1

        # if not root:
        #     return True
        # return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        # 1.2 自底向上 O(n) O(n)
        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            if left_height == -1:
                return -1
            right_height = dfs(root.right)
            if right_height == -1:
                return -1
            return max(left_height, right_height) + 1 if abs(left_height - right_height) <= 1 else -1
        return dfs(root) != -1