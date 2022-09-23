"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 1. 中序遍历

        if not root:
            return

        # 1.1 递归 O(N) O(N)
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)   
        
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

        # # 1.2 迭代 O(N) O(N)
        # stack = []
        # pre = head = None
        # cur = root

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     top = stack.pop()
        #     if pre:
        #         top.left, pre.right = pre, top
        #     else:
        #         head = top
        #     pre = top
        #     cur = top.right

        # head.left, pre.right = pre, head
        # return head