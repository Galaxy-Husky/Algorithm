class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 迭代 栈
        cur, stack, res = root, [], []
        while cur or stack:  # cur非空-> 还有左子树；stack非空->还有右子树
            while cur:
                stack.append(cur)
                cur = cur.right
            top = stack.pop()
            res.append(top.val)
            if len(res) == k:
                return res[-1]
            cur = top.left
        """ # 递归
        self.res, self.k = None, k
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            if self.k > 0:
                dfs(root.left)
        dfs(root)
        return self.res """