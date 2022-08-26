# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归
        '''if not inorder:
            return
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root'''

        # 优化-哈希表存储索引
        def recur(root, left, right):  # 根节点在preorder的索引 子树在inorder的左边界和右边界索引
            if left > right:
                return
            root_val = preorder[root]
            node = TreeNode(root_val)
            index = d[root_val]
            node.left = recur(root + 1, left, index - 1)
            node.right = recur(root + (index - left) + 1, index + 1, right)
            return node

        d = {}
        for i, val in enumerate(inorder):
            d[val] = i
        return recur(0, 0, len(inorder) - 1)
