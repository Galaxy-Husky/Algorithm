class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # # 1. DFS 递归 O(N) O(N)

        # def dfs(root, target, path):
        #     if not root:
        #         return
        #     if not root.left and not root.right and root.val == target:
        #         path.append(root.val)
        #         res.append(path)
        #     dfs(root.left, target-root.val, path+[root.val])
        #     dfs(root.right, target-root.val, path+[root.val])

        # res = []
        # dfs(root, target, [])
        # return res

        # 2. BFS 迭代 O(N) O(N)
        if not root:
            return []
        res = []
        stack = [(root, target-root.val, [root.val])]
        while stack:
            cur, tsum, path = stack.pop()
            if not cur.left and not cur.right and tsum==0:
                res.append(path)
            if cur.right:
                stack.append((cur.right, tsum-cur.right.val, path+[cur.right.val]))
            if cur.left:
                stack.append((cur.left, tsum-cur.left.val, path+[cur.left.val]))
        return res  