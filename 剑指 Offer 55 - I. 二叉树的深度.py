def maxDepth(self, root: TreeNode) -> int:
        '''# DFS 递归
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1'''
        
        # BFS 迭代
        '''if not root:
            return 0
        depth = 0
        q = [root]
        while q:
            depth += 1
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return depth'''

        if not root:
            return 0
        depth = 0
        q = [root]
        while q:
            size  = len(q)
            for _ in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

