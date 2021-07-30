# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        '''# 递归法
        return self.reversePrint(head.next) + [head.val] if head else []'''

        # 栈
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]