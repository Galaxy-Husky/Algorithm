class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # # 1. 递归 中序遍历倒序 O(N) O（N）
        # def dfs(root):
        #     if not root or self.count == 0:
        #         return
        #     dfs(root.right)
        #     self.count -= 1
        #     if self.count == 0:
        #         self.res = root.val
        #     dfs(root.left)

        # self.res, self.count = None, k
        # dfs(root)
        
        # return self.res

        # 2. 迭代 O(N) O(N)
        count = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            top = stack.pop()
            count += 1
            if count == k:
                return top.val
            cur = top.left