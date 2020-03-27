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

        """ # 回溯 1
        self.res, self.k = None, k
        def dfs(head):
            if not head:
                return 
            dfs(head.next)
            self.k -= 1
            if self.k == 0:
                self.res = head
        dfs(head)
        return self.res """
    
    """ # 回溯 2
    def __init__(self):
        self.count = 0
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        node = self.getKthFromEnd(head.next, k)
        self.count += 1
        if self.count == k:
            return head
        return node """

        
