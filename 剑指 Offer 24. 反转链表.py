# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代-双指针
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

        '''# 递归
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res'''