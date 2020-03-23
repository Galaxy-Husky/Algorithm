class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 栈
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]