import collections
import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 迭代 双端队列 O(N) O(N)
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            size = len(deque)
            tmp = collections.deque()
            for _ in range(size):
                node = deque.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res
        