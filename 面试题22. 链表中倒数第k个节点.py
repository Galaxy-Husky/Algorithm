class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针
        slow = quick = head
        for i in range(k):
            quick = quick.next
        while quick:
            quick = quick.next
            slow = slow.next
        return slow