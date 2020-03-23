class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 双指针
        pre = dummy = ListNode(-1)
        cur = dummy.next = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
                return dummy.next
            pre, cur = cur, cur.next