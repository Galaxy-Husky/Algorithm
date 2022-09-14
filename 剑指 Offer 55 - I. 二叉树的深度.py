def maxDepth(self, root: TreeNode) -> int:
        # # 1. DFS 递归 O(N) O(N)
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        # 2. BFS 迭代 O(N) O(N)
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
