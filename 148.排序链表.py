#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode.cn/problems/sort-list/description/
#
# algorithms
# Medium (66.25%)
# Likes:    1759
# Dislikes: 0
# Total Accepted:    340.5K
# Total Submissions: 514K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# 
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 归并排序 O(NlogN)

        def merge(left, right):
            h = dummy = ListNode()
            while left and right:
                if left.val < right.val:
                    h.next = left
                    left = left.next
                else:
                    h.next = right
                    right = right.next
                h = h.next
            h.next = left if left else right
            return dummy.next

        # # 1.1 自顶向下（递归，空间复杂度O(logN)）
        # # 快慢指针找中点
        # if not head or not head.next:
        #     return head
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # mid = slow.next
        # slow.next = None
        # return merge(self.sortList(head), self.sortList(mid))


        # 1.2 自底向上 （空间复杂度O(1)）
        h = head
        length = 0
        while h:
            h = h.next
            length += 1

        interval = 1
        dummy = ListNode(0, head)       
        while interval < length:
            prev, cur = dummy, dummy.next
            while cur:
                h1 = cur
                for _ in range(1, interval):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                h2 = cur.next
                cur.next = None
                cur = h2
                for _ in range(1, interval):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                
                succ = None
                if cur:
                    succ = cur.next
                    cur.next = None

                merged = merge(h1, h2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                cur = succ
            interval *= 2
        return dummy.next

# @lc code=end

