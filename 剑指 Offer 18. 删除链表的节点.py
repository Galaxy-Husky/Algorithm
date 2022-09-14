# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # # 1. 双指针 O(N) O(1)
        # if head.val == val:
        #     return head.next
        # pre, cur = head, head.next
        # while cur:
        #     if cur.val == val:
        #         pre.next = cur.next
        #         return head
        #     pre, cur = cur, cur.next

        # 2. 单指针+哑结点 O(N) O(1)
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur:
            if cur.next.val == val:
                cur.next = cur.next.next
                return dummy.next
            cur = cur.next
        