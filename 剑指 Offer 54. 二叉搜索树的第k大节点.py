class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 二叉搜索树的中序遍历为递增序列-中序遍历倒序的第k个节点
        '''# 迭代 栈
        cur, stack, res = root, [], []
        while cur or stack:  # cur非空-> 还有左子树；stack非空->还有右子树
            while cur:
                stack.append(cur)
                cur = cur.right
            top = stack.pop()
            res.append(top.val)
            if len(res) == k:
                return res[-1]
            cur = top.left'''
            
        # 递归
        def dfs(root):
            if not root or self.count == 0:
                return
            dfs(root.right)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
            dfs(root.left)

        self.res, self.count = None, k
        dfs(root)
        
        return self.res