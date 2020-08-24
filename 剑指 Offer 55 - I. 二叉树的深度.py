def maxDepth(self, root: TreeNode) -> int:
        # DFS 递归
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        """ # DFS 非递归 栈
        cur, stack, depth, max_depth = root, [], 0, 0
        while cur or stack:
            while cur:
                depth += 1
                stack.append((cur, depth))
                cur = cur.left
            top, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            cur = top.right
        return max_depth """
        
        """ # BFS 迭代 队列 
        if not root:
            return 0
        depth = 0
        q = [root]
        while q:
            depth += 1
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth """
