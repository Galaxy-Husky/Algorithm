"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    global d 
    d = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 1. 拼接+拆分 O(N) O(1)
        if not head:
            return

        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res

    # # 2. 哈希表

    # # 2.1 递归 O(N) O(N)
    #     if not head:
    #         return None

    #     if head not in d:
    #         new = Node(head.val)
    #         d[head] = new
    #         new.next = self.copyRandomList(head.next)
    #         new.random = self.copyRandomList(head.random)
    #     return d[head]

    # # 2.2 迭代 O(N) O(N)
    #     if not head:
    #         return 
    #     cache = {}
    #     cur = head
    #     while cur:
    #         cache[cur] = Node(cur.val)
    #         cur = cur.next
    #     cur = head
    #     while cur:
    #         cache[cur].next = cache.get(cur.next)
    #         cache[cur].random = cache.get(cur.random)
    #         cur = cur.next
    #     return cache[head]