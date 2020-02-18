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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # new_head = reverse(curl_l -> cur_r)
        # last_tail -> new_head
        # new_tail = cur_l -> next_head
        dummy = last_tail =  cur_r = ListNode(-1)
        dummy.next = head

        while True:
            for i in range(k):
                cur_r = cur_r.next
                if cur_r is None:
                    return dummy.next
            cur_l = last_tail.next
            next_head = cur_r.next
            cur_r.next = None
            last_tail.next = self.reverse(cur_l)
            cur_l.next, last_tail, cur_r =  next_head, cur_l, cur_l
        
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre
            
        
# @lc code=end

