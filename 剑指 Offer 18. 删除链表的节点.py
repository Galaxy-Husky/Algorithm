# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        '''# 双指针+哑结点
        pre = dummy = ListNode(-1)
        cur = dummy.next = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
                return dummy.next
            pre, cur = cur, cur.next'''

        # 双指针
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        pre.next = cur.next
        return head
        