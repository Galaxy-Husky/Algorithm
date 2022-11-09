#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (56.11%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 66.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 示例 :
# 
# 给定这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 说明 :
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(N) O(1)
        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

        dummy = ListNode(-1, head)
        prev = end = dummy
        while end.next:
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            left_node = prev.next
            right_node = end.next
            prev.next = None
            end.next = None
            reverse(left_node)
            prev.next = end
            left_node.next = right_node
            prev = end = left_node
        return dummy.next   
# @lc code=end

