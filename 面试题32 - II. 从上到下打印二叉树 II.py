class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS 队列
        if not root:
            return []
        res = []
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res