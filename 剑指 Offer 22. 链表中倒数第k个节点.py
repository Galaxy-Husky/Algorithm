# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢双指针
        slow = quick = head
        for _ in range(k):
            quick = quick.next
        while quick:
            quick = quick.next
            slow = slow.next
        return slow
