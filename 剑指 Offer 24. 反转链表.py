# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # # 1. 迭代-双指针 O(N) O(1)
        # pre, cur = None, head

        # # 1.1 
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        # return pre

        # # 1.2
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur 
        #     cur = tmp 
        # return pre 

        # 2. 递归 O(N) O(N)

        # 2.1
        # if not head or not head.next:
        #     return head
        # res = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return res

        # 2.2
        def recur(pre, cur):
            if not cur:
                return pre
            res = recur(cur, cur.next)
            cur.next = pre
            return res
        return recur(None, head)