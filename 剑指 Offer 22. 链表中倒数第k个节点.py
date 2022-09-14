# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # # 1. 顺序 O(N) O(1)
        # node = head
        # count = 0
        # while node:
        #     node = node.next
        #     count += 1
        # node = head
        # for _ in range(count-k):
        #     node = node.next
        # return node

        # 2. 快慢双指针 O(N) O(1)
        slow = quick = head
        for _ in range(k):
            quick = quick.next
        while quick:
            quick = quick.next
            slow = slow.next
        return slow
