class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 1. 迭代 O(N) O(N)
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

        # # 2. 递归 O(N) O(N)
        # res = []
        
        # def recur(node, depth):
        #     if not node:
        #         return
        #     if len(res) == depth:
        #         res.append([])
        #     res[depth].append(node.val)
        #     recur(node.left, depth+1)
        #     recur(node.right, depth+1)
        
        # recur(root, 0)
        # return res






        