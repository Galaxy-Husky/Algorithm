#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.77%)
# Likes:    508
# Dislikes: 0
# Total Accepted:    81K
# Total Submissions: 164.5K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 优先队列
        cur = dummy = ListNode(-1)
        pq = PriorityQueue()
        for index, node in enumerate(lists):
            if node:
                pq.put((node.val, index, node))
        while not pq.empty():
            val, index, node = pq.get()
            cur.next = node
            cur, node = cur.next, node.next
            if node:
                pq.put((node.val, index, node))
        return dummy.next

# @lc code=end
