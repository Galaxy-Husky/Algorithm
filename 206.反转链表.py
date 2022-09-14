#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.97%)
# Likes:    766
# Dislikes: 0
# Total Accepted:    156.8K
# Total Submissions: 234.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. 迭代-双指针 O(N) O(1)
        # pre, cur = None, head

        # # 1.1 
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        # return pre

        # # 1.2
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur 
        #     cur = tmp 
        # return pre 

        # 2. 递归 O(N) O(N)

        # 2.1
        # if not head or not head.next:
        #     return head
        # res = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return res

        # 2.2
        def recur(pre, cur):
            if not cur:
                return pre
            res = recur(cur, cur.next)
            cur.next = pre
            return res
        return recur(None, head)

# @lc code=end

