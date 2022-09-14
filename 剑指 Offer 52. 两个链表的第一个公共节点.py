# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # # 1. 哈希 O(m+n) O(m)
        # set_A = set()
        # cur = headA
        # while cur:
        #     set_A.add(cur)
        #     cur = cur.next
        # cur = headB
        # while cur:
        #     if cur in set_A:
        #         return cur
        #     cur = cur.next
        # return None

        # 2. 双指针 O(m+n) O(1) a + all + b = b + all + a
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p