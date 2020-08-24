class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre