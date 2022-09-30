#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (52.49%)
# Likes:    1526
# Dislikes: 0
# Total Accepted:    508.8K
# Total Submissions: 969K
# Testcase Example:  '[1,2,2,1]'
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,2,1]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
# 
# 
# 
# 
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # 1. 复制到列表 O(N) O(N)
        # vals = []
        # cur = head
        # while cur:
        #     vals.append(cur.val)
        #     cur = cur.next
        # return vals == vals[::-1]

        # 2. 快慢指针-反转前半链表 O(N) O(1)
        pre = None
        slow = fast = head
        while fast and fast.next:
            slow.next, pre, slow, fast = pre, slow, slow.next, fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
            

# @lc code=end

