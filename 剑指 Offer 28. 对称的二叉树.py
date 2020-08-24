class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ # DFS 递归
        if not root:
            return True
        def mirror(t1, t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            else:
                return mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
        return mirror(root.left, root.right) """
        # BFS 迭代 队列
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            l = q.pop(0)
            r = q.pop(0)
            if l == None and r == None:
                continue
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            q += [l.left, r.right, l.right, r.left]
        return True